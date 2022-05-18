from . import init_app
from 


app = init_app()


### Blueprints ####
app.register_blueprint(inventory_bp,url_prefix='/')