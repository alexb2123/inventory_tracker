from tokenize import ContStr
from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField

class ManageInventory(FlaskForm):
    sku=StringField('SKU')
    #cost=
    #tax=
    #retailer=
    #po=        
    None     