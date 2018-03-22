from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


SECRET_KEY = 'Sup3r$3cretkey'
UPLOAD_FOLDER = "./app/static/uploads"

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://aaxbdpaigwvzym:4351f5d0d6ef28c7d86157a3fd2748a063946905079f53154fea70584af6b57e@ec2-54-204-44-140.compute-1.amazonaws.com:5432/dehphtl0o8klc4"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cheyko:password@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
app.debug = True
from app import views


