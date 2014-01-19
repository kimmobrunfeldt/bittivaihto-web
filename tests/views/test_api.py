# -*- coding: utf-8 -*-
import json
from decimal import Decimal

from flask import url_for

from bittivaihto.models import SellOrder

from tests import ViewTestCase


valid_request_data = {
    'name': u'John Doe',
    'email': u'john.doe@email.com',
    'bank_account': u'CH93 0076 2011 6238 5295 7',
    'currency': u'btc',
    'sell_amount': '1.1'
}

invalid_request_data = {
    'name': u'John Doe',
    'email': u'john.doe@.com',
    'bank_account': u'CH93 0076 2011 6238 5295 7',
    'currency': u'btc',
    'sell_amount': 'amount'
}


class TestValidSellOrderPOST(ViewTestCase):
    def setup_method(self, method):
        super(TestValidSellOrderPOST, self).setup_method(method)
        self.response = self.client.post(
            url_for('api.create_sell_order'),
            data=json.dumps(valid_request_data)
        )

    def test_post_returns_201(self):
        assert self.response.status_code == 201

    def test_post_creates_a_sell_order(self):
        assert SellOrder.query.count() > 0

    def test_post_returns_created(self):
        assert self.response.data == u'Created'

    def test_created_sell_order_contains_right_data(self):
        sell_order = SellOrder.query.first()
        assert sell_order.name == u'John Doe'
        assert sell_order.email == u'john.doe@email.com'
        assert sell_order.bank_account == u'CH93 0076 2011 6238 5295 7'
        assert sell_order.currency == u'btc'
        assert sell_order.sell_amount == Decimal('1.1')


class TestInvalidUsersPOST(ViewTestCase):
    def test_no_data_returns_400(self):
        response = self.client.post(
            url_for('api.create_sell_order')
        )
        assert response.status_code == 400

    def test_invalid_data_returns_400(self):
        response = self.client.post(
            url_for('api.create_sell_order'),
            data=json.dumps(invalid_request_data)
        )
        assert response.status_code == 400

    def test_invalid_data_returns_errors(self):
        response = self.client.post(
            url_for('api.create_sell_order'),
            data=json.dumps(invalid_request_data)
        )
        errors = json.loads(response.data)
        assert u'email' in errors
        assert u'sell_amount' in errors
