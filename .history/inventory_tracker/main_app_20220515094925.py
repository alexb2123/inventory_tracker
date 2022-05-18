from . import init_app
from inventory_tracker.blueprints.inventory.views import 


app = init_app()


### Blueprints ####
app.register_blueprint(inventory_bp,url_prefix='/')