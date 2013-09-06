# -*- coding: utf-8 -*-
from ..extensions import db


class Round(db.Model):
    __tablename__ = 'round'

    id = db.Column(db.Integer, primary_key=True)

    winner_layer_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'layer.id',
            ondelete='RESTRICT',
            use_alter=True,
            name='fk_winner_layer_id'
        ),
        nullable=True
    )

    winner_layer = db.relationship(
        'Layer',
        primaryjoin='winner_layer_id == layer.id',
        foreign_keys=[winner_layer_id],
        uselist=False,
        post_update=True
    )

    start_date = db.Column(
        db.Date,
        nullable=False
    )

    end_date = db.Column(
        db.Date,
        nullable=False
    )
