from flask import render_template, Blueprint, request, session, redirect, url_for
from markupsafe import escape
from ..db.db import db
from ..models.UserApp import UserApp


login = Blueprint('login', __name__, template_folder='templates')


@login.get('/connexion')
def login_get():
    return render_template('login.html')


@login.post('/connexion')
def login_post():
    # Escape login form input
    user_email = escape(request.form['Email'])
    user_password = escape(request.form['Password'])
    # Search user from login input in database
    try:
        current_user: UserApp = db.session.execute(db.select(UserApp).filter_by(email=user_email)).scalar_one()
        # Return index if current user exist and current user password matches whith input password
        if current_user.password == user_password:
            session['username'] = user_email
            return redirect(url_for('index.index_get'))
        return render_template('login.html', error_log='Adresse e-mail ou mot de passe invalide')
    except Exception:
        return render_template('login.html', error_log='Adresse e-mail ou mot de passe invalide')
