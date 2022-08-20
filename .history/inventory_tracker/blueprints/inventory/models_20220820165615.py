from ... import db

class Inventory(db.Model):
    __tablename__ = "Inventory"
    __bind_key__ = "defaultdb"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ItemName = db.Column(db.String(300))
    ItemPrice = db.Column(db.Float)
    ItemTax = db.Column(db.Float)
    Retailer = db.Column(db.String(100))
    amazon_asin = db.Column(db.String(100))
    retailer_asin = db.Column(db.String(100))
    item_returned = db.Column(db.String(100))
    refunded_amount = db.Column(db.Float)
    order_number = db.Column(db.String(100))
    order_date = db.Column(db.String(100))
    bndl_qty = db.Column(db.Integer)
    rebate_used = db.Column(db.String(100))
    destination = db.Column(db.String(4))