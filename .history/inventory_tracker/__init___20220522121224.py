import os
from flask import Flask
from flask import 



app = Flask(__name__)

def init_app():
    with app.app_context():
        return app