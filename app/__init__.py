from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Define the path for the SQLite database
file_path = os.path.abspath(os.getcwd()) + "/todo.db"

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Import routes to register them
from app import routes
