import sqlalchemy as sa
from flask.ext.security import SQLAlchemyUserDatastore
from flask.ext.sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry
from sqlalchemy_defaults import Column, make_lazy_configured


db = SQLAlchemy()
sentry = Sentry(logging=True)

db.Column = Column
make_lazy_configured(sa.orm.mapper)

from .auth.models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
