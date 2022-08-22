from flask import Blueprint, render_template
from ... import app, db
from inventory_tracker.blueprints.inventory.forms import BulkUpload
import csv
from inventory_tracker.blueprints.inventory.models import Inventory
import os
from flask.helpers import flash, url_for
from werkzeug.utils import redirect, secure_filename

inventory_bp = Blueprint('inventory_bp', __name__, template_folder='templates')

@inventory_bp.route("/", methods=["GET", "POST"])
def manage_inventory():
    form = BulkUpload()    

    if form.validate_on_submit():
        the_csv_file = form.file.data
        the_csv_file.save('inventory_tracker/blueprints/inventory/temp_folder/tempfile.csv')

        with open('inventory_tracker/blueprints/inventory/temp_folder/tempfile.csv', 'r', encoding='utf-8-sig') as f:
            datareader = csv.DictReader(f)
            rmv_empty_row=[*filter(len,datareader)]
            values=rmv_empty_row
            for value in values:
                print(value)

            ins = db.insert(Inventory).values(values)
            print(str(ins))
            db.session.execute(ins)
            db.session.commit()
            db.session.close_all()
        
        os.remove('inventory_tracker/blueprints/inventory/temp_folder/tempfile.csv')
        flash('Uploaded Bulk File', 'success')
        return redirect(url_for('inventory_bp.manage_inventory'))

    return render_template("manage_inventory.html", form=form)

@inventory_bp.route("/prep_shipment", methods=["GET", "POST"])
def manage_inventory():
    pass