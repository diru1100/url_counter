import flask
from redis import Redis
from rq import Queue
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = flask.Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.create_all()
q = Queue(connection=Redis())

from app import routes, models