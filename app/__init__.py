from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize Flask app and SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app

app = create_app() 