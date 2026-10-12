"""YaCut application package — a link shortening service."""

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from yacut.settings import Config

app: Flask = Flask(__name__)
app.config.from_object(Config)
db: SQLAlchemy = SQLAlchemy(app)
migrate = Migrate(app, db)


from yacut import api_views, errorhandlers, models, views  # noqa: E402, F401
