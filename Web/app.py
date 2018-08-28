from flask import Flask
from flask import render_template
from flask import request
from flask import session
import data
app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      return data.active()
   else:
      return render_template("Login2.html")

@app.route("/eval", methods=['POST', 'GET'])
def startup():

    if request.method == "POST":
        att1 = request.form['att1']
        Qua1 = request.form['Qua1']
        Quan1 = request.form['Quan1']
        Coo1 = request.form['Coo1']
        Fol1 = request.form['Fol1']
        Total1 = int(att1) + int(Qua1) + int(Quan1) + int(Coo1) + int(Fol1)
        att2 = request.form['att2']
        Qua2 = request.form['Qua2']
        Quan2 = request.form['Quan2']
        Coo2 = request.form['Coo2']
        Fol2 = request.form['Fol2']
        Total2 = int(att2) + int(Qua2) + int(Quan2) + int(Coo2) + int(Fol2)
        att3 = request.form['att3']
        Qua3 = request.form['Qua3']
        Quan3 = request.form['Quan3']
        Coo3 = request.form['Coo3']
        Fol3 = request.form['Fol3']
        Total3 = int(att3) + int(Qua3) + int(Quan3) + int(Coo3) + int(Fol3)
        att4 = request.form['att4']
        Qua4 = request.form['Qua4']
        Quan4 = request.form['Quan4']
        Coo4 = request.form['Coo4']
        Fol4 = request.form['Fol4']
        Total4 = int(att4) + int(Qua4) + int(Quan4) + int(Coo4) + int(Fol4)

        return render_template("Temp.html", Total1=Total1, Total2=Total2,
        Total3=Total3, Total4=Total4)
    else:
        return render_template("Version3.html")

app.secret_key = '3rfguo982yt34h'


if __name__ == "__main__":
    app.run()
