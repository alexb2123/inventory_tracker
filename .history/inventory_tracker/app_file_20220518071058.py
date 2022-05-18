from .. import init_app
from inventory_tracker.blueprints.inventory.views import inventory_bp


app = init_app()


### Blueprints ####
app.register_blueprint(inventory_bp,url_prefix='/')