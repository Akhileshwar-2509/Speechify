# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # Set up the secret key for the app (make sure to change this in production)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite example, change for other DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Register blueprints (if you use blueprints, for example)
    # app.register_blueprint(auth_bp)
    
    # Import routes
    from app import routes

    return app
