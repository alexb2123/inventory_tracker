import os
from flask import Flask
from flask import SQLAlchemy




app = Flask(__name__)
db = SQLAlchemy()

def init_app():
    '''Construct the core app'''

    app = Flask(__name__)
    app.config['''']
    with app.app_context():
        return app