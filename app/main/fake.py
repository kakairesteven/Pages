from views import database_connection
from faker import Faker
fake = Faker()

def fake_data():
    # connect to database
    cnx = database_connection()
    mycursor = cnx.cursor()
    mycursor.execute("USE pages;")
    for i in range(1000):
        email = fake.email()
        surname = fake.last_name()
        first_name = fake.first_name()
        date_of_birth = fake()
        country = fake.country()
        
        query = "INSERT INTO client \
                    (email_address, surname, first_name, date_of_birth, country) \
                    VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(query, (email, surname, first_name, date_of_birth, country))
        cnx.commit()
        print(i + 'th value inserted')
        cnx.close()
        
fake_data()
