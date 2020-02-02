from flask import Flask,request,render_template
import pymysql
from flask_restful import Api

db =pymysql.connect("localhost","root","","flaskdb")

app = Flask(__name__)
api = Api(app)

@app.route('/')
def someName():
    cursor = db.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    results = cursor.fetchall()
   
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)