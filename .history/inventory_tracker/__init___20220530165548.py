import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager




app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
manager = Manager()

def init_app():
    '''Construct the core app'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URI1"
        )#os.getenv("SQLALCHEMY_DATABASE_URI1")#'mysql+pymysql://doadmin:AVNS_43F-8yARLhB1kfH@db-mysql-nyc3-64061-do-user-6928885-0.b.db.ondigitalocean.com:25060/defaultdb' #os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    


    db.init_app(app)
    migrate = Migrate(app,db, compare_type=True)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    with app.app_context():
        db.create_all()
        return app

    