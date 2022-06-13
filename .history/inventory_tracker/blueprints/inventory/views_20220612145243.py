from flask import Blueprint, render_template
from ... import app, db
from inventory_tracker.blueprints.inventory.forms import BulkUpload
import csv
from inventory_tracker.blueprints.inventory.models import Inventory

inventory_bp = Blueprint('inventory_bp', __name__, template_folder='templates')

@inventory_bp.route("/")
def manage_inventory():
    form = BulkUpload()    

    if form.validate_on_submit():
        the_csv_file = form.file.data
        the_csv_file.save('inventory_tracker/blueprints/inventory/temp_folder/tempfile.csv')

        with open('inventory_tracker/blueprints/inventory/temp_folder/tempfile.csv', 'r') as f:
            datareader = csv.DictReader(f)
            rmv_empty_row=[*filter(len,datareader)]
            values_map = map(rmv_empty_row)
            values=[*values_map]
            ins = db.insert(Inventory)
            db.session.ecevute(ins,values)
            
        None

    return render_template("manage_inventory.html")