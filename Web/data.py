import psycopg2
from flask import render_template
from flask import request
from flask import session
import nacl.pwhash

def active():
    conn = psycopg2.connect('host=137.99.253.210 user=pi dbname=feedback')
    cur = conn.cursor()

    cur.execute('select * from login where username=%s;', (request.form['username'],))
    results = cur.fetchone()
    psw = request.form['psw']
    res = nacl.pwhash.verify(results[3].encode(), psw.encode())
    print(len(results))
    if len(results)!=5:
        return render_template("Login2.html")

    elif res == False:
        return render_template("Login2.html")

    else:
        session['username'] = request.form['username']
        return render_template("Version3.html")
