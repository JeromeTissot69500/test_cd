from flask import render_template, Blueprint, session, redirect, url_for


index = Blueprint('index', __name__, template_folder='templates')

@index.get('/')
def index_get():
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login.login_get'))