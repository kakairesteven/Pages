from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # initialization
    db.init_app(app)
    
    # simple page
    # @app.route('/king')
    # def hello():
    #     return 'hello, king'
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
