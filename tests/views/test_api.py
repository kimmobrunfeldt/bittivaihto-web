# -*- coding: utf-8 -*-
import json

from flask import url_for

from bittivaihto.models import SellOrder
from bittivaihto.serializers import SellOrderSerializer

from tests import ViewTestCase


valid_request_data = {
    'username': u'username',
    'first_name': u'John',
    'last_name': u'Doe',
    'email': u'john.doe@email.com',
    'password': u'secret-password'
}

invalid_request_data = {
    'username': u'username',
    'first_name': u'John',
    'last_name': u'Doe',
    'email': u'john.doe@email.com',
    'password': u'secret-password'
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

    def test_post_returns_json_serialized_sell_order(self):
        sell_order = SellOrder.query.first()
        assert self.response.data == SellOrderSerializer(sell_order).json

    def test_created_sell_order_contains_right_data(self):
        pass


class TestInvalidUsersPOST(ViewTestCase):
    def test_no_data_returns_400(self):
        self.response = self.client.post(
            url_for('api.create_sell_order')
        )
        assert self.response.status_code == 400

    def test_invalid_data_returns_400(self):
        self.response = self.client.post(
            url_for('api.create_sell_order'),
            data=json.dumps(invalid_request_data)
        )
        assert self.response.status_code == 400

    def test_invalid_data_returns_errors(self):
        self.response = self.client.post(
            url_for('api.create_sell_order'),
            data=json.dumps(invalid_request_data)
        )
        pass
