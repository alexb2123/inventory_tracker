from . import init_app


app = init_app()


### Blueprints ####
app.register_blueprint(landing_page,url_prefix='/')