from flask import Flask, render_template, request, session, url_for, redirect, jsonify
import pymysql

# Initialize the app for Flask
app = Flask(__name__)

# Set the secrete key
app.secret_key = '000'

# Connect to the database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='@0519China',
    db='dpr4pwc',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Function to get gdpr contents from databases
def gdpr(article):
    try:
        with conn.cursor() as cursor:
            conn.ping(reconnect=True)
            query1 = '''SELECT content FROM gdpr WHERE number = '%s';''' % pymysql.escape_string(article)
            cursor.execute(query1)
            content = cursor.fetchall()
            content = content[0]['content']
            query2 = '''SELECT CONCAT_WS('  ', number, title) AS title FROM gdpr WHERE number = '%s';''' % pymysql.escape_string(article)
            cursor.execute(query2)
            title = cursor.fetchall()
            title = title[0]['title']
    finally:
        conn.close()
    return title, content

# Function to get ccpa contents from databases
def ccpa(title):
    try:
        with conn.cursor() as cursor:
            conn.ping(reconnect=True)
            query1 = '''SELECT content FROM ccpa WHERE title = '%s';''' % pymysql.escape_string(title)
            cursor.execute(query1)
            content = cursor.fetchall()
            content = content[0]['content']
    finally:
        conn.close()
    return title, content

# Function to get pipeda contents from databases
def pipeda(title):
    try:
        with conn.cursor() as cursor:
            conn.ping(reconnect=True)
            query1 = '''SELECT content FROM pipeda WHERE title RLIKE '%s';''' % pymysql.escape_string(title)
            cursor.execute(query1)
            content = cursor.fetchall()
            content = content[0]['content']
    finally:
        conn.close()
    return content

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/pipeda1')
def pipeda1():
    content = pipeda('Principle 1')
    return render_template('pipeda1.html', content=content)

@app.route('/pipeda2')
def pipeda2():
    content = pipeda('Principle 2')
    return render_template('pipeda2.html', content=content)

@app.route('/pipeda3')
def pipeda3():
    content = pipeda('Principle 3')
    return render_template('pipeda3.html', content=content)

@app.route('/pipeda4')
def pipeda4():
    content = pipeda('Principle 4')
    return render_template('pipeda4.html', content=content)

@app.route('/pipeda5')
def pipeda5():
    content = pipeda('Principle 5')
    return render_template('pipeda5.html', content=content)

@app.route('/pipeda6')
def pipeda6():
    content = pipeda('Principle 6')
    return render_template('pipeda6.html', content=content)

@app.route('/pipeda7')
def pipeda7():
    content = pipeda('Principle 7')
    return render_template('pipeda7.html', content=content)

@app.route('/pipeda8')
def pipeda8():
    content = pipeda('Principle 8')
    return render_template('pipeda8.html', content=content)

@app.route('/pipeda9')
def pipeda9():
    content = pipeda('Principle 9')
    return render_template('pipeda9.html', content=content)

@app.route('/pipeda10')
def pipeda10():
    content = pipeda('Principle 10')
    return render_template('pipeda10.html', content=content)

@app.route('/ccpa1')
def ccpa1():
    title, content = ccpa('1798.100.')
    return render_template('ccpa100.html', title=title, content=content)

@app.route('/ccpa2')
def ccpa2():
    title, content = ccpa('1798.105.')
    return render_template('ccpa105.html', title=title, content=content)

@app.route('/ccpa3')
def ccpa3():
    title, content = ccpa('1798.110.')
    return render_template('ccpa110.html', title=title, content=content)

@app.route('/ccpa4')
def ccpa4():
    title, content = ccpa('1798.115.')
    return render_template('ccpa115.html', title=title, content=content)

@app.route('/ccpa5')
def ccpa5():
    title, content = ccpa('1798.120.')
    return render_template('ccpa120.html', title=title, content=content)

@app.route('/ccpa6')
def ccpa6():
    title, content = ccpa('1798.125.')
    return render_template('ccpa125.html', title=title, content=content)

@app.route('/ccpa7')
def ccpa7():
    title, content = ccpa('1798.130.')
    return render_template('ccpa130.html', title=title, content=content)

@app.route('/ccpa8')
def ccpa8():
    title, content = ccpa('1798.135.')
    return render_template('ccpa135.html', title=title, content=content)

@app.route('/ccpa9')
def ccpa9():
    title, content = ccpa('1798.140.')
    return render_template('ccpa140.html', title=title, content=content)

@app.route('/ccpa10')
def ccpa10():
    title, content = ccpa('1798.145.')
    return render_template('ccpa145.html', title=title, content=content)

@app.route('/ccpa11')
def ccpa11():
    title, content = ccpa('1798.150.')
    return render_template('ccpa150.html', title=title, content=content)

@app.route('/ccpa12')
def ccpa12():
    title, content = ccpa('1798.155.')
    return render_template('ccpa155.html', title=title, content=content)

@app.route('/ccpa13')
def ccpa13():
    title, content = ccpa('1798.160.')
    return render_template('ccpa160.html', title=title, content=content)

@app.route('/ccpa14')
def ccpa14():
    title, content = ccpa('1798.165.')
    return render_template('ccpa165.html', title=title, content=content)

@app.route('/ccpa15')
def ccpa15():
    title, content = ccpa('1798.170.')
    return render_template('ccpa170.html', title=title, content=content)

@app.route('/ccpa16')
def ccpa16():
    title, content = ccpa('1798.175.')
    return render_template('ccpa175.html', title=title, content=content)

@app.route('/ccpa17')
def ccpa17():
    title, content = ccpa('1798.180.')
    return render_template('ccpa180.html', title=title, content=content)

@app.route('/ccpa18')
def ccpa18():
    title, content = ccpa('1798.185.')
    return render_template('ccpa185.html', title=title, content=content)

@app.route('/ccpa19')
def ccpa19():
    title, content = ccpa('1798.190.')
    return render_template('ccpa190.html', title=title, content=content)

@app.route('/ccpa20')
def ccpa20():
    title, content = ccpa('1798.192.')
    return render_template('ccpa192.html', title=title, content=content)

@app.route('/ccpa21')
def ccpa21():
    title, content = ccpa('1798.194.')
    return render_template('ccpa194.html', title=title, content=content)

@app.route('/ccpa22')
def ccpa22():
    title, content = ccpa('1798.196.')
    return render_template('ccpa196.html', title=title, content=content)

@app.route('/ccpa23')
def ccpa23():
    title, content = ccpa('1798.198.')
    return render_template('ccpa198.html', title=title, content=content)

@app.route('/ccpa24')
def ccpa24():
    title, content = ccpa('1798.199.')
    return render_template('ccpa199.html', title=title, content=content)

# gdpr
@app.route('/gdpr1')
def gdpr1():
    title, content = gdpr('Article 1')
    return render_template('gdpr1.html', title=title, content=content)

@app.route('/gdpr2')
def gdpr2():
    title, content = gdpr('Article 2')
    return render_template('gdpr2.html', title=title, content=content)

@app.route('/gdpr3')
def gdpr3():
    title, content = gdpr('Article 3')
    return render_template('gdpr3.html', title=title, content=content)

@app.route('/gdpr4')
def gdpr4():
    title, content = gdpr('Article 4')
    return render_template('gdpr4.html', title=title, content=content)

@app.route('/gdpr5')
def gdpr5():
    title, content = gdpr('Article 5')
    return render_template('gdpr5.html', title=title, content=content)

@app.route('/gdpr6')
def gdpr6():
    title, content = gdpr('Article 6')
    return render_template('gdpr6.html', title=title, content=content)

@app.route('/gdpr7')
def gdpr7():
    title, content = gdpr('Article 7')
    return render_template('gdpr7.html', title=title, content=content)

@app.route('/gdpr8')
def gdpr8():
    title, content = gdpr('Article 8')
    return render_template('gdpr8.html', title=title, content=content)

@app.route('/gdpr9')
def gdpr9():
    title, content = gdpr('Article 9')
    return render_template('gdpr9.html', title=title, content=content)

@app.route('/gdpr10')
def gdpr10():
    title, content = gdpr('Article 10')
    return render_template('gdpr10.html', title=title, content=content)

@app.route('/gdpr11')
def gdpr11():
    title, content = gdpr('Article 11')
    return render_template('gdpr11.html', title=title, content=content)

@app.route('/gdpr12')
def gdpr12():
    title, content = gdpr('Article 12')
    return render_template('gdpr12.html', title=title, content=content)

@app.route('/gdpr13')
def gdpr13():
    title, content = gdpr('Article 13')
    return render_template('gdpr13.html', title=title, content=content)

@app.route('/gdpr14')
def gdpr14():
    title, content = gdpr('Article 14')
    return render_template('gdpr14.html', title=title, content=content)

@app.route('/gdpr15')
def gdpr15():
    title, content = gdpr('Article 15')
    return render_template('gdpr15.html', title=title, content=content)

@app.route('/gdpr16')
def gdpr16():
    title, content = gdpr('Article 16')
    return render_template('gdpr16.html', title=title, content=content)

@app.route('/gdpr17')
def gdpr17():
    title, content = gdpr('Article 17')
    return render_template('gdpr17.html', title=title, content=content)

@app.route('/gdpr18')
def gdpr18():
    title, content = gdpr('Article 18')
    return render_template('gdpr18.html', title=title, content=content)

@app.route('/gdpr19')
def gdpr19():
    title, content = gdpr('Article 19')
    return render_template('gdpr19.html', title=title, content=content)

@app.route('/gdpr20')
def gdpr20():
    title, content = gdpr('Article 20')
    return render_template('gdpr20.html', title=title, content=content)

@app.route('/gdpr21')
def gdpr21():
    title, content = gdpr('Article 21')
    return render_template('gdpr21.html', title=title, content=content)

@app.route('/gdpr22')
def gdpr22():
    title, content = gdpr('Article 22')
    return render_template('gdpr22.html', title=title, content=content)

@app.route('/gdpr23')
def gdpr23():
    title, content = gdpr('Article 23')
    return render_template('gdpr23.html', title=title, content=content)

@app.route('/gdpr24')
def gdpr24():
    title, content = gdpr('Article 24')
    return render_template('gdpr24.html', title=title, content=content)

@app.route('/gdpr25')
def gdpr25():
    title, content = gdpr('Article 25')
    return render_template('gdpr25.html', title=title, content=content)

@app.route('/gdpr26')
def gdpr26():
    title, content = gdpr('Article 26')
    return render_template('gdpr26.html', title=title, content=content)

@app.route('/gdpr27')
def gdpr27():
    title, content = gdpr('Article 27')
    return render_template('gdpr27.html', title=title, content=content)

@app.route('/gdpr28')
def gdpr28():
    title, content = gdpr('Article 28')
    return render_template('gdpr28.html', title=title, content=content)

@app.route('/gdpr29')
def gdpr29():
    title, content = gdpr('Article 29')
    return render_template('gdpr29.html', title=title, content=content)

@app.route('/gdpr5')
def gdpr30():
    title, content = gdpr('Article 30')
    return render_template('gdpr30.html', title=title, content=content)

@app.route('/gdpr31')
def gdpr31():
    title, content = gdpr('Article 31')
    return render_template('gdpr31.html', title=title, content=content)

@app.route('/gdpr32')
def gdpr32():
    title, content = gdpr('Article 32')
    return render_template('gdpr32.html', title=title, content=content)

@app.route('/gdpr33')
def gdpr33():
    title, content = gdpr('Article 33')
    return render_template('gdpr33.html', title=title, content=content)

@app.route('/gdpr34')
def gdpr34():
    title, content = gdpr('Article 34')
    return render_template('gdpr34.html', title=title, content=content)

@app.route('/gdpr35')
def gdpr35():
    title, content = gdpr('Article 35')
    return render_template('gdpr35.html', title=title, content=content)

@app.route('/gdpr36')
def gdpr36():
    title, content = gdpr('Article 36')
    return render_template('gdpr36.html', title=title, content=content)

@app.route('/gdpr37')
def gdpr37():
    title, content = gdpr('Article 37')
    return render_template('gdpr37.html', title=title, content=content)

@app.route('/gdpr38')
def gdpr38():
    title, content = gdpr('Article 38')
    return render_template('gdpr38.html', title=title, content=content)

@app.route('/gdpr39')
def gdpr39():
    title, content = gdpr('Article 39')
    return render_template('gdpr39.html', title=title, content=content)

@app.route('/gdpr40')
def gdpr40():
    title, content = gdpr('Article 40')
    return render_template('gdpr40.html', title=title, content=content)

@app.route('/gdpr41')
def gdpr41():
    title, content = gdpr('Article 41')
    return render_template('gdpr41.html', title=title, content=content)

@app.route('/gdpr42')
def gdpr42():
    title, content = gdpr('Article 42')
    return render_template('gdpr42.html', title=title, content=content)

@app.route('/gdpr43')
def gdpr43():
    title, content = gdpr('Article 43')
    return render_template('gdpr43.html', title=title, content=content)

@app.route('/gdpr44')
def gdpr44():
    title, content = gdpr('Article 44')
    return render_template('gdpr44.html', title=title, content=content)

@app.route('/gdpr45')
def gdpr45():
    title, content = gdpr('Article 45')
    return render_template('gdpr45.html', title=title, content=content)

@app.route('/gdpr46')
def gdpr46():
    title, content = gdpr('Article 46')
    return render_template('gdpr46.html', title=title, content=content)

@app.route('/gdpr47')
def gdpr47():
    title, content = gdpr('Article 47')
    return render_template('gdpr47.html', title=title, content=content)

@app.route('/gdpr48')
def gdpr48():
    title, content = gdpr('Article 48')
    return render_template('gdpr48.html', title=title, content=content)

@app.route('/gdpr49')
def gdpr49():
    title, content = gdpr('Article 49')
    return render_template('gdpr49.html', title=title, content=content)

@app.route('/gdpr50')
def gdpr50():
    title, content = gdpr('Article 50')
    return render_template('gdpr50.html', title=title, content=content)

@app.route('/gdpr51')
def gdpr51():
    title, content = gdpr('Article 51')
    return render_template('gdpr51.html', title=title, content=content)

@app.route('/gdpr52')
def gdpr52():
    title, content = gdpr('Article 52')
    return render_template('gdpr52.html', title=title, content=content)

@app.route('/gdpr53')
def gdpr53():
    title, content = gdpr('Article 53')
    return render_template('gdpr53.html', title=title, content=content)

@app.route('/gdpr54')
def gdpr54():
    title, content = gdpr('Article 54')
    return render_template('gdpr54.html', title=title, content=content)

@app.route('/gdpr55')
def gdpr55():
    title, content = gdpr('Article 55')
    return render_template('gdpr55.html', title=title, content=content)

@app.route('/gdpr56')
def gdpr56():
    title, content = gdpr('Article 56')
    return render_template('gdpr56.html', title=title, content=content)

@app.route('/gdpr57')
def gdpr57():
    title, content = gdpr('Article 57')
    return render_template('gdpr57.html', title=title, content=content)

@app.route('/gdpr58')
def gdpr58():
    title, content = gdpr('Article 58')
    return render_template('gdpr58.html', title=title, content=content)

@app.route('/gdpr59')
def gdpr59():
    title, content = gdpr('Article 59')
    return render_template('gdpr59.html', title=title, content=content)

@app.route('/gdpr60')
def gdpr60():
    title, content = gdpr('Article 60')
    return render_template('gdpr60.html', title=title, content=content)

@app.route('/gdpr61')
def gdpr61():
    title, content = gdpr('Article 61')
    return render_template('gdpr61.html', title=title, content=content)

@app.route('/gdpr62')
def gdpr62():
    title, content = gdpr('Article 62')
    return render_template('gdpr62.html', title=title, content=content)

@app.route('/gdpr63')
def gdpr63():
    title, content = gdpr('Article 63')
    return render_template('gdpr63.html', title=title, content=content)

@app.route('/gdpr64')
def gdpr64():
    title, content = gdpr('Article 64')
    return render_template('gdpr64.html', title=title, content=content)

@app.route('/gdpr65')
def gdpr65():
    title, content = gdpr('Article 65')
    return render_template('gdpr65.html', title=title, content=content)

@app.route('/gdpr66')
def gdpr66():
    title, content = gdpr('Article 66')
    return render_template('gdpr66.html', title=title, content=content)

@app.route('/gdpr67')
def gdpr67():
    title, content = gdpr('Article 67')
    return render_template('gdpr67.html', title=title, content=content)

@app.route('/gdpr68')
def gdpr68():
    title, content = gdpr('Article 68')
    return render_template('gdpr68.html', title=title, content=content)

@app.route('/gdpr69')
def gdpr69():
    title, content = gdpr('Article 69')
    return render_template('gdpr69.html', title=title, content=content)

@app.route('/gdpr70')
def gdpr70():
    title, content = gdpr('Article 70')
    return render_template('gdpr70.html', title=title, content=content)

@app.route('/gdpr71')
def gdpr71():
    title, content = gdpr('Article 71')
    return render_template('gdpr72.html', title=title, content=content)

@app.route('/gdpr73')
def gdpr73():
    title, content = gdpr('Article 73')
    return render_template('gdpr73.html', title=title, content=content)

@app.route('/gdpr74')
def gdpr74():
    title, content = gdpr('Article 74')
    return render_template('gdpr74.html', title=title, content=content)

@app.route('/gdpr75')
def gdpr75():
    title, content = gdpr('Article 75')
    return render_template('gdpr75.html', title=title, content=content)

@app.route('/gdpr76')
def gdpr76():
    title, content = gdpr('Article 76')
    return render_template('gdpr76.html', title=title, content=content)

@app.route('/gdpr77')
def gdpr77():
    title, content = gdpr('Article 77')
    return render_template('gdpr77.html', title=title, content=content)

@app.route('/gdpr78')
def gdpr78():
    title, content = gdpr('Article 78')
    return render_template('gdpr78.html', title=title, content=content)

@app.route('/gdpr79')
def gdpr79():
    title, content = gdpr('Article 79')
    return render_template('gdpr79.html', title=title, content=content)

@app.route('/gdpr80')
def gdpr80():
    title, content = gdpr('Article 80')
    return render_template('gdpr80.html', title=title, content=content)

@app.route('/gdpr81')
def gdpr81():
    title, content = gdpr('Article 81')
    return render_template('gdpr81.html', title=title, content=content)

@app.route('/gdpr82')
def gdpr82():
    title, content = gdpr('Article 82')
    return render_template('gdpr82.html', title=title, content=content)

@app.route('/gdpr83')
def gdpr83():
    title, content = gdpr('Article 83')
    return render_template('gdpr83.html', title=title, content=content)

@app.route('/gdpr84')
def gdpr84():
    title, content = gdpr('Article 84')
    return render_template('gdpr84.html', title=title, content=content)

@app.route('/gdpr85')
def gdpr85():
    title, content = gdpr('Article 85')
    return render_template('gdpr85.html', title=title, content=content)

@app.route('/gdpr86')
def gdpr86():
    title, content = gdpr('Article 86')
    return render_template('gdpr86.html', title=title, content=content)

@app.route('/gdpr87')
def gdpr87():
    title, content = gdpr('Article 87')
    return render_template('gdpr87.html', title=title, content=content)

@app.route('/gdpr88')
def gdpr88():
    title, content = gdpr('Article 88')
    return render_template('gdpr88.html', title=title, content=content)

@app.route('/gdpr89')
def gdpr89():
    title, content = gdpr('Article 89')
    return render_template('gdpr89.html', title=title, content=content)

@app.route('/gdpr90')
def gdpr90():
    title, content = gdpr('Article 90')
    return render_template('gdpr90.html', title=title, content=content)

@app.route('/gdpr91')
def gdpr91():
    title, content = gdpr('Article 91')
    return render_template('gdpr91.html', title=title, content=content)

@app.route('/gdpr92')
def gdpr92():
    title, content = gdpr('Article 92')
    return render_template('gdpr92.html', title=title, content=content)

@app.route('/gdpr93')
def gdpr93():
    title, content = gdpr('Article 93')
    return render_template('gdpr93.html', title=title, content=content)

@app.route('/gdpr94')
def gdpr94():
    title, content = gdpr('Article 94')
    return render_template('gdpr94.html', title=title, content=content)

@app.route('/gdpr95')
def gdpr95():
    title, content = gdpr('Article 95')
    return render_template('gdpr95.html', title=title, content=content)

@app.route('/gdpr96')
def gdpr96():
    title, content = gdpr('Article 96')
    return render_template('gdpr96.html', title=title, content=content)

@app.route('/gdpr97')
def gdpr97():
    title, content = gdpr('Article 97')
    return render_template('gdpr97.html', title=title, content=content)

@app.route('/gdpr98')
def gdpr98():
    title, content = gdpr('Article 98')
    return render_template('gdpr98.html', title=title, content=content)

@app.route('/gdpr99')
def gdpr99():
    title, content = gdpr('Article 99')
    return render_template('gdpr99.html', title=title, content=content)



if __name__ == '__main__':
    app.run(debug=True)
