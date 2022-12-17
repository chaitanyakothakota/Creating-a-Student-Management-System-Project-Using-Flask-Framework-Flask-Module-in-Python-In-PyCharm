from flask import Flask, render_template, request, redirect
import pymysql

x = Flask(__name__)


@x.route('/')
def index():
    try:
        db = pymysql.connect(host="localhost", user="root", password="", database="studentdata")
        cu = db.cursor()
        sql = "select * from student"
        cu.execute(sql)
        data = cu.fetchall()
        return render_template('home.html', d=data)
    except Exception as e:
        print("Error:", e)


@x.route('/form')
def form():
    return render_template('create.html')


@x.route('/store', methods=['POST'])
def store():
    si = request.form['STUDENT REGID']
    sn = request.form['STUDENT NAME']
    ss = request.form['STUDENT SURNAME']
    sc = request.form['STUDENT COURSE']
    con = request.form['STUDENT CONTACT']
    try:
        db = pymysql.connect(host="localhost", user="root", password="", database="studentdata")
        cus = db.cursor()
        insertsql = "insert into student(regno,name,surname,course,contact)values('{}','{}','{}','{}','{}')".format(si,sn,ss,sc,con)
        cus.execute(insertsql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print('error', e)


@x.route('/edit/<rrid>')
def edit(rrid):
    try:
        db = pymysql.connect(host="localhost", user="root", password="", database="studentdata")
        cu = db.cursor()
        sql = "select * from student where rid= '{}'".format(rrid)
        cu.execute(sql)
        data = cu.fetchone()
        return render_template('edit.html', d=data)

    except Exception as e:
        print("Error:", e)


@x.route('/update/<rrid>', methods=['GET','POST'])
def update(rrid):
    si = request.form.get['STUDENT REGID']
    sn = request.form['STUDENT NAME']
    ss = request.form['STUDENT SURNAME']
    sc = request.form['STUDENT COURSE']
    con = request.form['STUDENT CONTACT']
    try:
        db = pymysql.connect(host="localhost", user="root", password="", database="studentdata")
        cu = db.cursor()
        sql = "update student SET regno='{}',name='{}',surname='{}',course='{}',contact='{}' where rid='{}'".format(si,sn,ss,sc,con,rrid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print("Error:", e)


@x.route('/delete/<rrid>')
def delete(rrid):
    try:
        db = pymysql.connect(host="localhost", user="root", password="", database="studentdata")
        cu = db.cursor()
        sql = "delete from student where rid={}".format(rrid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print("Error:", e)


if __name__=='__main__':
    x.run(debug=True)

