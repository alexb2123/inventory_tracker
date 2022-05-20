from flask import Blueprint, render_template
from ... import app

inventory_bp = Blueprint('inventory_bp', __name__, template_folder='templates')

@
def landing():
    return render_template()