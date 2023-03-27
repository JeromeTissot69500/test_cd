from flask import render_template, Blueprint, redirect, url_for, session, request
from markupsafe import escape
from ..db.db import db
from ..models.UserApp import UserApp


user_account = Blueprint('user_account', __name__, template_folder='templates')


@user_account.get('/<string:email>')
def user_account_get(email):
    if 'username' in session:
        email = escape(email)
        # Search user from email slug in database
        try:
            current_user: UserApp = db.session.execute(db.select(UserApp).filter_by(email=email)).scalar_one()
        except Exception: 
            return redirect(url_for('index.index_get'))
        # Return user account with information
        return render_template('user_account.html', current_user=current_user)
    return redirect(url_for('login.login_get'))


@user_account.post('/update-account')
def user_account_post():
    if 'username' in session:
        # Escape user_account form input
        user_entry = {name: escape(value) for name, value in request.form.items()}
        # Update user information in db
        try:
            current_user: UserApp = db.session.execute(db.select(UserApp).filter_by(email=session['username'])).scalar_one()
            current_user.assure_number = user_entry['AssureNumber']
            current_user.last_name = user_entry['LastName']
            current_user.first_name = user_entry['FirstName']
            current_user.birthday = user_entry['Birthday']
            current_user.address = user_entry['Address']
            current_user.phone_number = user_entry['PhoneNumber']
            current_user.license_number = user_entry['LicenseNumber']
            current_user.email = user_entry['Email']
            db.session.commit()
        except Exception: 
            return redirect(url_for('user_account.html', current_user=current_user))
        return redirect(url_for('index.index_get'))
    return redirect(url_for('login.login_get'))
    
