from flask import Blueprint, render_template
from ... import app

inventory_bp = Blueprint('inventory_bp', __name__, template_folder='templates')

@inventory_bp.route("/")
def manage_inventory():
    
    return render_template("manage_inventory.html")