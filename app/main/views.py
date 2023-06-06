# from .. import db
from . import main
from flask import render_template, request, redirect, url_for
from .forms import RegistrationForm
from faker import Faker

# from mysql.connector.cursor import MySQLCursor
import mysql.connector


@main.route("/", methods=("GET", "POST"))
def index():
    return render_template("index.html")


db = "pages"
# password = 'kakaire'

def database_connection():
    cnx = mysql.connector.connect(
        host="localhost",
        user="kakaire",
        password="kakaire",
        database="pages",
        # use_unicode=False
    )
    return cnx


@main.route("/query", methods=["GET", "POST"])
def query_database():
    cnx = database_connection()
    mycursor = cnx.cursor()
    mycursor.execute("USE pages;")
    mycursor.execute("SELECT * FROM client;")
    # print(type(mycursor))
    tableData = []
    for dbName in mycursor:
        tableData.append(dbName)
        # print(dbName[0])
    print(tableData)
    return render_template("dbPrint.html", tableData=tableData)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    print('Request method', request.method)
    if request.method == 'POST':
        # form = RegistrationForm()
        cnx = database_connection()
        mycursor = cnx.cursor()
        mycursor.execute('USE pages;')
        email = request.form['email']
        surname = request.form['surname']
        first_name = request.form['first_name']
        date_of_birth = request.form['date_of_birth']
        country = request.form['country']
        print(email, surname, first_name, date_of_birth, country)

        query = "INSERT INTO client \
                    (email_address, surname, first_name, date_of_birth, country) \
                    VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(query, (email, surname, first_name, date_of_birth, country))
        cnx.commit()
        print('Inserted')
        cnx.close()
        return render_template('user.html')
    return render_template('register.html', form=form)

@main.route('/signIn', methods=['GET', 'POST'])
def signIn():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        default_password = '1234'
        print(email)
        cnx = database_connection()
        mycursor = cnx.cursor()
        mycursor.execute('USE pages;')
        mycursor.execute('SELECT email_address FROM client WHERE email_address = %(email_address)s;',\
                         {'email_address': email})
        user = mycursor.fetchone()
        print(user)
        if user is None:
            print('email required')
        else:
            print(user, ' signing in ...')
        return render_template('user.html')
    return render_template('index.html')

@main.route('/fake', methods=['POST', 'GET']) 
def fake_data():
    fake = Faker()
    # connect to database
    cnx = database_connection()
    mycursor = cnx.cursor()
    mycursor.execute("USE pages;")
    for i in range(1000):
        email = fake.email()
        surname = fake.last_name()
        first_name = fake.first_name()
        date_of_birth = fake.date()
        country = fake.country()
        
        query = "INSERT INTO client \
                    (email_address, surname, first_name, date_of_birth, country) \
                    VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(query, (email, surname, first_name, date_of_birth, country))
        cnx.commit()
        print(i,'th value inserted')
    cnx.close()

    return render_template('fake.html')
