from flask import Flask, url_for, request, render_template,redirect
import api
import os
import re
import mariadb



app = Flask(__name__)


@app.route('/register', methods =['GET', 'POST'])
def register():
    def check_register(attribut, msg_list, form_correct):
        return_value = ""
        if attribut in request.method:
            return_value = request.form['attribut']
        else:
            msg_list.append("please insert a " + attribut)
            form_correct.status = False
        return return_value

    class Checker:
        def __init__(self):
            status = True

    form_correct = Checker()
    msg_list = []

    if request.method == 'POST':
        first_name = check_register('first_name', msg_list, form_correct)
        last_name = check_register('last_name', msg_list, form_correct)
        email = check_register('email', msg_list, form_correct)
        phone_no = check_register('phone_no', msg_list, form_correct)
        password = check_register('password', msg_list, form_correct)
        street = check_register('street', msg_list, form_correct)
        street_no = check_register('street_no', msg_list, form_correct)
        zipcode = check_register('zipcode', msg_list, form_correct)
        city = check_register('city', msg_list, form_correct)

        con = api.connect_to_DB()
        cursor = con.cursor()

        if not form_correct.status:
            return render_template('register.html', msg_list=msg_list)
        else:


            query1 = f"INSERT INTO Test_User (first_name, last_name, email, phone_no, password, street, street_no, zipcode, city) VALUES ('{first_name}', '{last_name}', '{email}', '{phone_no}', '{password}', '{street}', '{street_no}', {zipcode}, '{city}')"

            cursor.execute(query1)
            con.commit()
            con.close()
            return render_template('you_are_registered.html')
    else:
        return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)

'''
	if request.method == 'POST':
		first_name = request.form['first_name']
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

		query1 = f"INSERT INTO Test_User (first_name, last_name, email, phone_no, password, street, street_no, zipcode, city) VALUES ('{first_name}', '{last_name}', '{email}', '{phone_no}', '{password}', '{street}', '{street_no}', {zipcode}, '{city}')"


		cursor.execute(query1)
		con.commit()
		con.close()


		return redirect("/")

	return render_template('register.html')

if __name__ == "__main__":
	app.run(debug=True)


def check_register(attribut, msg_list, form_correct):
    return_value = ""
    if attribut in request.method:
        return_value = request.name()
    else:
        msg_list.append("please insert a " + attribut)
        form_correct.status = False
    return return_value

class Checker:
    def __init__(self):
        status = True

form_correct = Checker()
masg_list = []

if request.method == "POST":
    first_name = check_register('first_name', msg_list, form_correct):
    sir_name = check_register("firstname", msg_list, form_correct):
    email = check_register("firstname", msg_list, form_correct):

if not form_correct.status:
    return render.template(register.html, msg_list=msg_list)
else:
    return render.template(you_are_registered.html)
'''