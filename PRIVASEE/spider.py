import logging
import random
import re

import bs4
import pymysql
import requests

logging.basicConfig(level=logging.INFO)

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '@0519China'
DB_DB = 'dpr4pwc'

# UA pool
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]


def _fetch_url(url):
    headers = {'user-agent': random.choice(USER_AGENT_LIST)}

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = bs4.BeautifulSoup(resp.content, 'html.parser')
    return soup

def crawl_pipeda(db_table):
    conn = pymysql.connect(host=DB_HOST,
                           user=DB_USER,
                           password=DB_PASSWORD,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor,
                           autocommit=True)
    try:
        with conn.cursor() as cursor:
            conn.ping(reconnect=True)
            # create database if not exists
            sql = "CREATE DATABASE IF NOT EXISTS `%s`;" % pymysql.escape_string(DB_DB)
            cursor.execute(sql)
            # select database
            conn.select_db(DB_DB)
            # drop table if exists
            sql = "DROP TABLE IF EXISTS `%s`" % pymysql.escape_string(db_table)
            cursor.execute(sql)
            # create table
            sql = """
                            CREATE TABLE `%s` (
                                `id` INT NOT NULL AUTO_INCREMENT,
                                `title` VARCHAR(200) NOT NULL,
                                `content` TEXT,
                                PRIMARY KEY (`id`)
                            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
                        """ % pymysql.escape_string(db_table)
            cursor.execute(sql)
            logging.info('DB initialized')

            # fetch index
            soup = _fetch_url(
                'https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/p_principle/')
            all_entries = soup.find('section', class_='col-md-8 pull-right').contents[-2]
            for child in all_entries.find_all('h2'):
                title = child.text
                soup2 = _fetch_url("http://priv.gc.ca" + child.find('a').attrs.get('href'))
                content = str(soup2.find('section', class_='col-md-8 pull-right'))
                query = "INSERT INTO `%s`(`title`, `content`) VALUES ('%s', '%s')" % (
                    db_table,
                    pymysql.escape_string(title),
                    pymysql.escape_string(content)
                )
                cursor.execute(query)
                logging.info("saved contents %s" % title)
    finally:
        logging.info("all tasks done")
        conn.close()


def crawl_ccpa(db_table):
    conn = pymysql.connect(host=DB_HOST,
                           user=DB_USER,
                           password=DB_PASSWORD,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor,
                           autocommit=True)
    try:
        with conn.cursor() as cursor:
            conn.ping(reconnect=True)
            # create database if not exists
            sql = "CREATE DATABASE IF NOT EXISTS `%s`;" % pymysql.escape_string(DB_DB)
            cursor.execute(sql)
            # select database
            conn.select_db(DB_DB)
            # drop table if exists
            sql = "DROP TABLE IF EXISTS `%s`" % pymysql.escape_string(db_table)
            cursor.execute(sql)
            # create table
            sql = """
                            CREATE TABLE `%s` (
                                `id` INT NOT NULL AUTO_INCREMENT,
                                `title` VARCHAR(200) NOT NULL,
                                `content` TEXT,
                                PRIMARY KEY (`id`)
                            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
                        """ % pymysql.escape_string(db_table)
            cursor.execute(sql)
            logging.info('DB initialized')

            # fetch ccpa content
            soup = _fetch_url(
                'http://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5')
            all_entries = soup.find('div', id='manylawsections').contents[3]
            title = []
            for child in all_entries.find_all('div'):
                if child.find('a') != None:
                    s = child.find("a").text
                    title.append(s)
                    logging.info('saved title %s' % s)
            for h in soup("h6"):
                h.extract()
            l = len(title)
            for child in all_entries.find_all('div'):
                if child.find('p') != None:
                    query = "INSERT INTO `%s`(`title`, `content`) VALUES ('%s', '%s')" % (
                        db_table,
                        pymysql.escape_string(title[0]),
                        pymysql.escape_string(str(child))
                    )
                    cursor.execute(query)
                    title.pop(0)
                    logging.info('saved content %s' % str(l-len(title)))
        logging.info('all tasks completed')

    finally:
        conn.close()

def crawl_gdpr(db_table):
    conn = pymysql.connect(host=DB_HOST,
                           user=DB_USER,
                           password=DB_PASSWORD,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor,
                           autocommit=True)

    try:
        with conn.cursor() as cursor:
            # create database if not exists
            sql = "CREATE DATABASE IF NOT EXISTS `%s`;" % pymysql.escape_string(DB_DB)
            cursor.execute(sql)
            # select database
            conn.select_db(DB_DB)
            # drop table if exists
            sql = "DROP TABLE IF EXISTS `%s`" % pymysql.escape_string(db_table)
            cursor.execute(sql)
            # create table
            sql = """
                CREATE TABLE `%s` (
                    `id` INT NOT NULL AUTO_INCREMENT,
                    `level` INT NOT NULL,
                    `number` VARCHAR(10) NOT NULL,
                    `title` VARCHAR(200) NOT NULL,
                    `content` TEXT,
                    PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
            """ % pymysql.escape_string(db_table)
            cursor.execute(sql)
            logging.info('DB initialized')

            # fetch index
            soup = _fetch_url('https://gdpr-info.eu/')
            all_entries = soup.find('div', class_='liste-inhaltsuebersicht dsgvo').contents
            logging.info('fetched %s entries from index' % len(all_entries))
            for child in all_entries:
                if not isinstance(child, bs4.element.Tag):
                    continue
                # level 1
                if 'kapitel' in child.attrs.get('class'):
                    level = 1
                    number = child.find('span', class_='nummer').text
                    title = child.find('span', class_='titel').text
                    content = ''
                # level 2
                elif 'abschnitt' in child.attrs.get('class'):
                    level = 2
                    number = child.find('span', class_='nummer').text
                    title = child.find('span', class_='titel').text
                    content = ''
                # level 3
                elif 'artikel' in child.attrs.get('class'):
                    level = 3
                    number = child.find('span', class_='nummer').text
                    title = child.find('span', class_='titel').text
                    soup2 = _fetch_url(child.find('a').attrs.get('href'))
                    content = str(soup2.find('div', class_='entry-content').contents[1])
                # unknown level
                else:
                    logging.warning('unknown level')
                sql = "INSERT INTO `%s` (`level`, `number`, `title`, `content`) VALUES ('%s', '%s', '%s', '%s')" % (
                    db_table,
                    level,
                    pymysql.escape_string(number),
                    pymysql.escape_string(title),
                    pymysql.escape_string(content) if content else None)
                cursor.execute(sql)
                logging.info('saved %s - %s...' % (number, title[:10]))
        logging.info('all tasks completed')
    finally:
        conn.close()


def crawl_pdpa(db_table):
    conn = pymysql.connect(host=DB_HOST,
                           user=DB_USER,
                           password=DB_PASSWORD,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor,
                           autocommit=True)

    try:
        with conn.cursor() as cursor:
            # create database if not exists
            sql = "CREATE DATABASE IF NOT EXISTS `%s`;" % pymysql.escape_string(DB_DB)
            cursor.execute(sql)
            # select database
            conn.select_db(DB_DB)
            # drop table if exists
            sql = "DROP TABLE IF EXISTS `%s`" % pymysql.escape_string(db_table + '_content')
            cursor.execute(sql)
            sql = "DROP TABLE IF EXISTS `%s`" % pymysql.escape_string(db_table + '_index')
            cursor.execute(sql)
            # create table
            sql = """
                CREATE TABLE `%s` (
                    `id` INT NOT NULL AUTO_INCREMENT,
                    `content` TEXT,
                    PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
            """ % (pymysql.escape_string(db_table) + '_content')
            cursor.execute(sql)
            sql = """
                CREATE TABLE `%s` (
                    `id` INT NOT NULL AUTO_INCREMENT,
                    `level` INT NOT NULL,
                    `title` VARCHAR(200) NOT NULL,
                    `href` VARCHAR(20) NOT NULL,
                    PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
            """ % (pymysql.escape_string(db_table) + '_index')
            cursor.execute(sql)
            logging.info('DB initialized')

            # fetch index
            soup = _fetch_url('https://sso.agc.gov.sg/Act/PDPA2012')
            content = str(soup.find('div', id='legis'))
            sql = "INSERT INTO `%s` (`content`) VALUES ('%s')" % (db_table + '_content', pymysql.escape_string(content))
            cursor.execute(sql)

            # fetch index
            for item in soup.find('ul', id='toc').find_all('a'):
                title = re.sub(r' {2,}', ' ', re.sub(r'[\t\r\n]', '', item.text)).strip()
                href = item.attrs.get('href')
                if not (title and href):
                    continue
                if title.startswith('Part'):
                    level = 1
                elif title.startswith('Division'):
                    level = 2
                elif title[0].isdigit():
                    level = 3
                else:
                    logging.warning('ambiguous title %s, set to level 1 by default' % title)
                    level = 1
                sql = "INSERT INTO `%s` (`level`, `title`, `href`) VALUES ('%s', '%s', '%s')" % (
                    db_table + '_index',
                    level,
                    pymysql.escape_string(title),
                    pymysql.escape_string(href))
                cursor.execute(sql)
        logging.info('all tasks completed')
    finally:
        conn.close()


def main():
    #crawl_gdpr(db_table='gdpr')
    #crawl_pdpa(db_table='pdpa')
    #crawl_ccpa(db_table='ccpa')
    crawl_pipeda(db_table='pipeda')

if __name__ == '__main__':
    main()
