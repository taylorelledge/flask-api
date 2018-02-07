from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DB_URI'] = 'sqlite:////temp/test.db'
app.config['WTF_CSRF_SECRET_KEY'] = 'fuck the celtics'
app.config['LDAP_PROVIDER_URL'] = 'insert LDAP server here'
app.config['LDAP_PROTOCOL_VERSION'] = 3
db = SQLAlchemy(app)

app.secret_key = 'fuck the giants'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#from my_app.auth.views import auth
#app.register_blueprint(auth) 

from app import routes
