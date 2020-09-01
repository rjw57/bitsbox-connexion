from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .app import application

db = SQLAlchemy(application)
migrate = Migrate(application, db)
