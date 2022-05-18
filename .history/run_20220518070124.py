from . import init_app


app = init_app()


### Blueprints ####
app.register_blueprint(inventory_bp,url_prefix='/')