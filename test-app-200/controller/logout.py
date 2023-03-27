from flask import Blueprint, session, redirect, url_for



logout = Blueprint('logout', __name__, template_folder='templates')


@logout.get('/deconnexion')
def logout_get():
    # Remove user session
    session.pop('username', None)
    return redirect(url_for('login.login_get'))