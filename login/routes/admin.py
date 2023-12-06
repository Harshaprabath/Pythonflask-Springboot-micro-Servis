
from services.auth import *


@app.route('/')
def home():
    return handle_home()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return handle_login()

@app.route('/logout')
def logout():
    return handle_logout()