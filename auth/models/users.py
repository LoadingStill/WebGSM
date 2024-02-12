# Import necessary modules
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from yourapp import db, login

# Define the User model
class User(UserMixin, db.Model):
    __tablename__ = 'users'  # Specify the table name

    # Define the columns for the table
    id = db.Column(db.Integer, primary_key=True)  # User ID
    username = db.Column(db.String(64), unique=True, index=True)  # Username
    password_hash = db.Column(db.String(128))  # Hashed password

    # Method to set the hashed password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Method to check if the hashed password matches the actual password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Function to load a user given the ID
@login.user_loader
def load_user(id):
    return User.query.get(int(id))  # Return the user object
