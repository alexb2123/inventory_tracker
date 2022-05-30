from ... import db

class Inventory(db.Model):
    __tablename__ = "Inventory"
    __bind_key__ = 