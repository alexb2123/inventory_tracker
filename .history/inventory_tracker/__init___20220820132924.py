import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3





app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()


def init_app():
    '''Construct the core app'''

    app = Flask(__name__)
#    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
#        "DATABASE_URI1"
#        )#os.getenv("SQLALCHEMY_DATABASE_URI1")#'mysql+pymysql://doadmin:AVNS_43F-8yARLhB1kfH@db-mysql-nyc3-64061-do-user-6928885-0.b.db.ondigitalocean.com:25060/defaultdb' #os.getenv("SQLALCHEMY_DATABASE_URI")
    database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    SECRET_KEY= os.urandom(32)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_BINDS"] = {

    'defaultdb': os.environ.get('DATABASE_URI1'),
    #'content': os.environ.get('SQLALCHEMY_DATABASE_URI2'),
    #'applicant_tracker':os.environ.get('SQLALCHEMY_DATABASE_URI3')
    #
    } 
    


    db.init_app(app)
    migrate = Migrate(app,db)

    with app.app_context():
        db.create_all()
        return app

    