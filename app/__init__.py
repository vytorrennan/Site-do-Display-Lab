from flask import Flask
from config import Config

from app.extensions import db
from app.pages import bp as pages_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(pages_bp)

    return app