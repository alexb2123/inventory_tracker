from ... import db

class Inventory(db.Model):
    __tablename__ = "Inventory"
    __bind_key__ = "purchase_orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String(100))
    item_price = db.Column
    