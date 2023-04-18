''' Flask admin extension '''
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView  
from iqsheets_app import db
from .models import User, OAuth, Prompt, Template, MyAdminIndexView, AnalyticsView, TemplatesUploadView
from werkzeug.security import generate_password_hash
    
### Init Flask-Admin functions ### 

def create_admin(db):
    admin = Admin(name="IQSheet Admin", template_mode="bootstrap4", index_view=MyAdminIndexView())
    
    # Add views
    admin.add_view(ModelView(User, db.session, endpoint="users_admin"))
    admin.add_view(ModelView(OAuth, db.session, endpoint="oauth_admin"))
    admin.add_view(ModelView(Prompt, db.session))
    admin.add_view(ModelView(Template, db.session))
    admin.add_view(AnalyticsView(name='Analytics', endpoint='analytics'))
    admin.add_view(TemplatesUploadView(name='Template Upload', endpoint='templates'))
    return admin

def create_admin_user(username, email, password):
    if not password:
        raise ValueError('No ADMIN_USER_PASSWORD environment variable set')

    admin_user = User(username=username, email=email, password=password)
    admin_user.is_admin = True
    admin_user.is_confirmed = True
    admin_user.premium = True
    admin_user.confirmed_on = datetime.now()
    db.session.add(admin_user)
    db.session.commit()

    return admin_user

