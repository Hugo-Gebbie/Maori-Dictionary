from flask import Flask, render_template, request, session, redirect
import sqlite3
from sqlite3 import Error
from flask_bcrypt import Bcrypt

DB_NAME = "smile.db"

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "banana"

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

        return None

def is_logged_in():
    pass

@app.route('/')
def render_homepage():
    return render_template('Home.html', logged_in=is_logged_in())

@app.route('/menu')
def render_menu_page():
    return render_template('Menu.html')
    # connect to database
    con = create_connection(DB_NAME)

    # select what you want from the table
    query = 'SELECT name, description, volume, price, image FROM product'

    cur = con.cursor()
    cur.execute(query)
    product_list = cur.fetchall()
    con.close()

    return render_template('menu.html', product=product_list)

@app.route('/contact')
def render_contact_page():
    return render_template("Contact.html")

@app.route('/login')
def render_login_page():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def render_signup_page():
    print(request.form)
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    return render_template('signup.html')

app.run(host='0.0.0.0')
