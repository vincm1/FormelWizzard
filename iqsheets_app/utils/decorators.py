from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user

def check_confirmed_mail(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_confirmed is False:
            flash('Bitte bestätige deine Anmeldung!', 'warning')
            return redirect(url_for('user.unconfirmed'))
        return func(*args, **kwargs)

    return decorated_function