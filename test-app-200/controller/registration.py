from flask import render_template, Blueprint, request, redirect, url_for
from markupsafe import escape
from ..models.UserApp import UserApp
from ..db.db import db
from datetime import datetime as dt


registration = Blueprint('registration', __name__, template_folder='templates')


@registration.get('/inscription')
def registration_get():
    return render_template('registration.html')


@registration.post('/inscription')
def registration_post():
    # Escape registration form input
    user_entry = {name: escape(value) for name, value in request.form.items()}
    # Create user from registration form input
    user_birthday = dt.strptime(user_entry['Birthday'],"%Y-%m-%d")
    user = UserApp(None, user_entry['AssureNumber'], user_entry['LastName'], user_entry['FirstName'], user_birthday, 
                   user_entry['Address'], user_entry['PhoneNumber'], user_entry['LicenseNumber'], user_entry['Email'], user_entry['Password'])
    try:
        db.session.add(user)
        db.session.commit()
    except Exception:
        return redirect(url_for('registration.registration_get'))
    return redirect(url_for('login.login_get'))