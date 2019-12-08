from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

__version__ = "1.0.0.0"
db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from testwork.home import bp as home_bp
    app.register_blueprint(home_bp)

    from testwork.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


from testwork import models
