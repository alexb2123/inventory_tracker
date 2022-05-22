import os
from flask import Flask
from flask import SQLAlchemy




app = Flask(__name__)
db = SQLAlchemy()

def init_app():
    
    with app.app_context():
        return app