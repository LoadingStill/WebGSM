from flask import Blueprint
from flask_login import LoginManager

# Create a Flask Blueprint which will define views and forms
auth = Blueprint('auth', __name__)

# Flask-Login initialization
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from .models.user import User
    return User.query.get(int(user_id))

# Import the routes module, which we haven't written yet
from . import routes
