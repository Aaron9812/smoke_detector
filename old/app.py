from flask import Flask, render_template, request, redirect, url_for, session
import api
import re
import mariadb
import dashboard

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    msg=""
    if request.method == "POST" and "email" in request.form and "password" in request.form:
        username = request.form["email"]
        password = request.form["password"]
        
        con = api.connect_to_DB()
        cursor = con.cursor()
        try:   
            cursor.execute(f"SELECT * FROM users WHERE email = '{username}' AND password = '{password}'")
        except mariadb.Error as e:
            print(f"Error: {e}")

        account = cursor.fetchone()

        if account:
            session["loggedin"] = True
            session['id'] = account[0]
            session['username'] = account[3]
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        con = api.connect_to_DB
        cursor = con.cursor()
        try:   
            cursor.execute(f"SELECT * FROM users WHERE username = {username} AND password = {password}")
        except mariadb.Error as e:
            print(f"Error: {e}")

        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route("/dashboard")
def dashboard():
    return init_dashboard(server)

if __name__ == "__main__":
    app.secret_key = '12'
    app.run(debug=True)