from flask import Blueprint
from ... import app

inventory_bp = Blueprint('inventory_bp', __name__, template_folder='templates')

def landing()