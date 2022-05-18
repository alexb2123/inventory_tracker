import os
from flask import Flask



app = Flask(__name__)

def init__app():
    with app.app_context():
        return app