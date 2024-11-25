from flask import Flask 
app= Flask(__name__)
from app import routes, models
from config import Config
from app.forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)  
