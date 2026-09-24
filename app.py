from flask import Flask, request, render_template, redirect, url_for, session, Response, flash
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
import UserData
import os

app = Flask(__name__)


@app.route('/' , methods = ['GET' , 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        user_data = UserData.find_user(user)
        if user_data:
            if user_data[1] == user and check_password_hash(user_data[2], password):
                session['user'] = user
                return redirect(url_for("dashboard"))
            else:
                return render_template("index.html", error = "Invalid Creditials")
        else:
            return render_template("index.html", error = "User not found")
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))        
    username = session.get("user")

    return render_template("dashboard.html", username = username)

@app.route('/signup', methods = ['GET' , 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        User_data = UserData.find_user(username)
        if User_data:
            return render_template("index.html", error = "Username already exists. Choose a different username.")
        UserData.add_data(username, password)
        flash("Registration successful!")
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route('/logout', methods = ['POST'])
def logout():
    session.pop("user", None)   #session.clear()
    return redirect(url_for("login"))
    
if __name__ == ("__main__"):
    app.run(debug=True)