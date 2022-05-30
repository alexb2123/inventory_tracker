import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
db = SQLAlchemy()

def init_app():
    '''Construct the core app'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://doadmin:AVNS_43F-8yARLhB1kfH@db-mysql-nyc3-64061-do-user-6928885-0.b.db.ondigitalocean.com:25060/defaultdb' #os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    


    db.init_app(app)

    with app.app_context():
        db.create_all()
        return app

    