import os
# csv (comma separated values) file
import csv

from flask import Flask, render_template, request, session
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# creating a session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# enter the path of the database if not in the same directory
# enter the URL of the database if database is online
engine = create_engine("sqlite:///TutorApp.db")
# engine = create_engine(os.getenv("TutorApp.db"))
db = scoped_session(sessionmaker(bind=engine))


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('layout.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	username = request.form.get('username')
	firstname = request.form.get('firstname')
	lastname = request.form.get('lastname')
	password = request.form.get('password')
	confirmedpassword = request.form.get('confirmedpassword')
	gender = ''
	email = request.form.get('email')
	phone = request.form.get('phone')
	securityQuestion = request.form.get('securityquestion')
	securityAnswer = request.form.get('securityans')
	db.execute("INSERT INTO Tutors (username, firstName, lastName, email, password, confirmedPassword, phone) VALUES (:username, :firstname, :lastname, :email, :password, :confirmedpass, :phone)",
            {"username": username, "firstname": firstname, "lastname": lastname, "email": email, "password": password, "confirmedpass": confirmedpassword, "phone": phone})
	db.commit()
	return render_template('layout.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	pass




def main():
	pass


if __name__=="__main__":
	app.run(debug=False)
