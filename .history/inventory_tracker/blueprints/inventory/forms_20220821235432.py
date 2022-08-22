from tokenize import ContStr
from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.fields.simple import SubmitField

'''Do I want to load '''


#class ManageInventory(FlaskForm):
#    #sku=StringField('SKU', Vali)
#    #cost=
#    #tax=
#    #retailer=
#    #po=        
#    None     

class BulkUpload(FlaskForm):    
    file = FileField('File:', validators=[FileRequired(), FileAllowed(upload_set=['csv'], message='Only CSV and XLS/XLSX files!')])
    submit = SubmitField('Submit')

class InventoryStats(FlaskForm):
    sdate