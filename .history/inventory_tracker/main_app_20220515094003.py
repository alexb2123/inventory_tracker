from . import init_app
from 


app = init_app()


### Blueprints ####
app.register_blueprint(inventory_,url_prefix='/')