# -*- coding: utf-8 -*-
from sqlalchemy.orm import backref
from sqlalchemy_utils import InstrumentedList

from ..extensions import db
from ..alchemy import FileType
from ..auth.models import User


class Layer(db.Model):
    __tablename__ = 'layer'

    #: NOTICE: in psql unique constraints don't prevent multiple NULL values,
    #: hence it is possible to have multiple layers where for example
    #: added_by_id=NULL and round_id=1
    __table_args__ = (
        db.UniqueConstraint('added_by_id', 'round_id'),
    )

    id = db.Column(db.Integer, primary_key=True)

    added_by_id = db.Column(
        db.Integer,
        db.ForeignKey(User.id, ondelete='CASCADE'),
        nullable=False
    )

    added_by = db.relationship(
        User,
        primaryjoin=added_by_id == User.id,
        backref=backref(
            'layers',
            cascade='all, delete-orphan',
            passive_deletes=True,
            collection_class=InstrumentedList
        )
    )

    round_id = db.Column(
        db.Integer,
        db.ForeignKey('round.id', ondelete='CASCADE'),
        nullable=False
    )

    round = db.relationship(
        'Round',
        backref=backref(
            'layers',
            cascade='all, delete-orphan',
            passive_deletes=True,
            collection_class=InstrumentedList
        )
    )

    created_at = db.Column(
        db.DateTime,
        auto_now=True,
        nullable=False
    )

    image = db.Column(FileType)