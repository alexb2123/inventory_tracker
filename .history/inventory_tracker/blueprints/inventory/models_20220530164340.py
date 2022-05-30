from ... import db

class Inventory(db.Model):
    __tablename__ = "Inventory"
    __bind_key__ = "purchase_orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_n = db.Column(db.String(100))
    item_p = db.Column(db.Float)
    item_tax = db.Column(db.Float)
    retailer = db.Column(db.String(100))
