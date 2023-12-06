# app.py

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
from services.auth import *
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key in production

mongo = conn(app)
#admin gI0bopwHhdHJlG1T
@app.route('/admin')
def home():
    return handle_home()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return handle_login(mongo)

@app.route('/logout')
def logout():
    return handle_logout()

@app.route('/forgetpassword', methods=['GET'])
def reset_user():
    return fogetpassword()

@app.route('/resetpassword', methods=['GET','POST'])
def reset_passwword():
    return resetpassword(mongo)

@app.route('/profile', methods=['GET'])
def user():
    return profile()

@app.route('/update_user', methods=['GET','POST'])
def update_user():
    return updateuser(mongo)

#gava back end

@app.route('/java', methods=['GET'])
def get_data_from_java():
    java_backend_url = 'http://localhost:9090/api/hello'  # Replace with your Java backend URL
    response = requests.get(java_backend_url)
    data_from_java = response.text
    return jsonify({'data_from_java': data_from_java})

#main 
if __name__ == '__main__':
    app.run(debug=True,port=8000)
