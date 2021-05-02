from flask import Flask, request, render_template,redirect
import os
import api
import re
import mariadb



app = Flask(__name__)


@app.route('/register', methods =['GET', 'POST'])

def register():
    if request.method == 'POST':
	    first_name = request.form['first_name']  # --> VarPython = request.form['VarHTML']
		last_name = request.form['last_name']
		email = request.form['email']
		phone_no = request.form['phone_no']
		password = request.form['password']
		street = request.form['street']
		street_no = request.form['street_no']
		zipcode = request.form['zipcode']
		city = request.form['city']

        con = api.connect_to_DB()
        cursor = con.cursor()

		query1 = "INSERT INTO Test_User(first_name, last_name, email, phone_no, password, street, street_no, zipcode, city) VALUES (first_name, last_name, email, phone_no, password, street, street_no, zipcode, city))"

		cursor.execute(query1)
		mysql.connection.commit()

		return redirect("/")

    return render_template('register.html')

if __name__ = "__main__":
    app.run()