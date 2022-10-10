from flask import Blueprint, render_template
from ... import app, db
from inventory_tracker.blueprints.inventory.forms import BulkUpload, InventoryStats
import csv
from inventory_tracker.blueprints.inventory.models import Inventory
import os
from flask.helpers import flash, url_for
from werkzeug.utils import redirect, secure_filename
from sqlalchemy import func

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
#            for value in values:
#                print(value)

            ins = db.insert(Inventory).values(values)
#            print(str(ins))
            db.session.execute(ins)
            db.session.commit()
            db.session.close_all()
        
        os.remove('inventory_tracker/blueprints/inventory/temp_folder/tempfile.csv')
        flash('Uploaded Bulk File', 'success')
        return redirect(url_for('inventory_bp.manage_inventory'))

    return render_template("manage_inventory.html", form=form)

@inventory_bp.route("/prep_shipment", methods=["GET", "POST"])
def prep_shipment():
    pass

@inventory_bp.route("/inventory_stats", methods=["GET", "POST"])
def inventory_stats():
#    form = InventoryStats()
#    start_date = form.sdate.data
#    end_date = form.edate.data
#
#    if form.validate_on_submit():
#        None
    #check orders placed based on order date range
    #check total spent based on date range
    #check total count based on date range

    total_spend = db.session.query(func.sum(Inventory.ItemPrice).label('total_spend')).first()
    print('total spend before returns')
    print('-------------')    
    print(total_spend.total_spend)

    total_returns= db.session.query(func.sum(Inventory.RefundedAmount).label('refund_total')).first()
    print('this is the type for returns')


    after_returns = (total_spend.total_spend - total_returns.refund_total)
    print('total spend after returns')
    print('-------------')
    print(after_returns)

    #item_count = db.session.query(func.count(Inventory.))

    return render_template("inventory_stats.xhtml", 
    total_spend=total_spend.total_spend, 
    total_refund=total_returns.refund_total, 
    after_refunds=after_returns)


@inventory_bp.route("/inventory_stats", methods=["GET", "POST"])
def modify_inventory():
    pass