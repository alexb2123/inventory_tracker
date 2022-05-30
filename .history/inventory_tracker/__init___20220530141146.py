import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
db = SQLAlchemy()

def init_app():
    '''Construct the core app'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = #os.environ.get("SQLALCHEMY_DATABASE_URI")
    


    db.init_app(app)

    with app.app_context():
        db.create_all()
        return app

    