import os
from flask import Flask
from flask import SQLAlchemy




app = Flask(__name__)
db = SQLAlchemy()

def init_app():
    '''Construct the core app'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 
    mysql://doadmin:AVNS_43F-8yARLhB1kfH@db-mysql-nyc3-64061-do-user-6928885-0.b.db.ondigitalocean.com:25060/defaultdb?ssl-mode=REQUIRED
    with app.app_context():
        return app