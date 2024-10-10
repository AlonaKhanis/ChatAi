import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)

    
    if config_name == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object(Config)

    db.init_app(app)
    
    # Initialize Migrate with app and db
    migrate.init_app(app, db)

    with app.app_context():
        from app.routes import main
        app.register_blueprint(main)

        db.create_all()  

    return app
