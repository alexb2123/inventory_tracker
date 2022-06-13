from flask import Blueprint, render_template
from ... import app
from inventory_tracker.blueprints.inventory.forms import BulkUpload

inventory_bp = Blueprint('inventory_bp', __name__, template_folder='templates')

@inventory_bp.route("/")
def manage_inventory():
    form = BulkUpload()    

    if form.validate_on_submit():
        the_csv_file = form.file.data
        the_csv_file.save(f'inventory_tracker/blueprints/inventory/temp_folder')
        None

    return render_template("manage_inventory.html")