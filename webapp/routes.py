from flask import Flask, render_template, request, redirect, url_for, session
from flask import current_app as app
import api
import re
import mariadb

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login(msg=""):
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
            return redirect(url_for('/dashapp/'))
        else:
            msg = 'Incorrect username / password !'
            return render_template('index.html', msg = msg)
        
    return render_template('index.html', msg = msg)


@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route("/livecheck")
def livecheck():
    if "loggedin" in session:
        return redirect(url_for('/dashapp/')) 
    else:
        return redirect(url_for('/login',msg="Please login first")) 


@app.route('/register', methods =['GET', 'POST'])
def register():
    if request.method == 'POST' and 'first_name' in request.form and 'last_name' in request.form and 'email' in request.form and 'phone_no' in request.form and 'password' in request.form and 'street' in request.form and 'street_no' in request.form and 'zipcode' in request.form and 'city' in request.form:

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_no = request.form['phone_no']
        password = request.form['password']
        street = request.form['street']
        street_no = request.form['street_no']
        zipcode = request.form['zipcode']
        city = request.form['city']
        
        address = street + street_no + zipcode + city
        country_code, geo_lat, geo_long = api.get_geo_data(address) 
        

        con = api.connect_to_DB()
        cursor = con.cursor()

        query1 = f"INSERT INTO users (first_name, last_name, email, phone_number, password, street, street_nr, zip, city, country_code, geo_lat, geo_long) VALUES ('{first_name}', '{last_name}', '{email}', '{phone_no}', '{password}', '{street}', '{street_no}', {zipcode}, '{city}', '{country_code}', {geo_lat}, {geo_long})"
        cursor.execute(query1)
        con.commit()
        con.close()

        return render_template('you_are_registered.html', name=first_name)

    else:
        return render_template('register.html')

