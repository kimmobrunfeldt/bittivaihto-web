# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy_utils import EmailType

from bittivaihto.extensions import db


class SellOrder(db.Model):
    __tablename__ = 'sell_order'

    id = db.Column(db.Integer, primary_key=True)

    # Possible values:
    # u'pending' - This is a new sell order. No email has been sent to the
    #              customer
    # u'waiting' - Waiting for customer to deposit and that 3 confirmations are
    #              received
    # u'transfering' - Transfering bitcoins from bittivaihto to market
    # u'selling' - Selling bitcoins in market
    # u'paying' - In process of paying the amount to customer
    status = db.Column(
        db.Unicode(255),
        nullable=False,
        default=u'pending',
        server_default=u'pending'
    )

    ordered_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    name = db.Column(
        db.Unicode(255),
        nullable=False
    )

    email = db.Column(
        EmailType(255),
        nullable=False
    )

    bank_account = db.Column(
        db.Unicode(255),
        nullable=False
    )

    sell_amount = db.Column(
        db.Integer,
        nullable=False
    )

    currency = db.Column(
        db.Unicode(10),
        nullable=False,
        default=u'BTC',
        server_default=u'BTC'
    )

    deposit_address = db.Column(
        db.Unicode(255),
        nullable=False
    )

    minimum_price = db.Column(
        db.Integer,
        nullable=True
    )

    maximum_time = db.Column(
        db.Integer,
        nullable=True
    )

    return_address = db.Column(
        db.Unicode(255),
        nullable=True
    )
