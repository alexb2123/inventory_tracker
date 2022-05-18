from . import init_app
from 


app = init_app()


### Blueprints ####
app.register_blueprint(landing_page_bp,url_prefix='/')