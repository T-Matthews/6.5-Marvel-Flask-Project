from flask import Flask	
from flask_migrate import Migrate
from config import Config
from .models import db, login
from .auth.routes import auth #import blueprint auth
from .api.routes import api
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth) #app and blueprint now communicate
app.register_blueprint(api)
from . import routes
migrate = Migrate(app,db)
login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please login to see this page'
login.login_message_category = 'danger'

