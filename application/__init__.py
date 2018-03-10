from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# setup database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from application import routes


from application import routes