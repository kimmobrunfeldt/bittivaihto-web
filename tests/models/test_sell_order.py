from datetime import datetime

from pytest import raises
from sqlalchemy.exc import IntegrityError

from bittivaihto.models import SellOrder

from tests import BaseTestCase
from tests.factories import SellOrderFactory


class TestSellOrderColumnExistences(BaseTestCase):
    def test_has_column_id(self):
        assert SellOrder.id

    def test_has_column_status(self):
        assert SellOrder.status

    def test_has_column_email(self):
        assert SellOrder.email

    def test_has_column_ordered_at(self):
        assert SellOrder.ordered_at

    def test_has_column_name(self):
        assert SellOrder.name

    def test_has_column_sell_amount(self):
        assert SellOrder.sell_amount

    def test_has_column_currency(self):
        assert SellOrder.currency

    def test_has_column_bank_account(self):
        assert SellOrder.bank_account

    def test_has_column_deposit_address(self):
        assert SellOrder.deposit_address

    def test_has_column_minimum_price(self):
        assert SellOrder.minimum_price

    def test_has_column_maximum_time(self):
        assert SellOrder.maximum_time

    def test_has_column_return_address(self):
        assert SellOrder.return_address


class TestSellOrderColumnRestrictions(BaseTestCase):
    def assert_required_attr(self, attr):
        kwargs = {}
        kwargs[attr] = None
        with raises(IntegrityError):
            SellOrderFactory(**kwargs)

    def assert_unique_attr(self, **kwargs):
        with raises(IntegrityError):
            SellOrderFactory(**kwargs)
            SellOrderFactory(**kwargs)

    def test_id_is_primary_key(self):
        self.assert_unique_attr(id=1)

    def test_name_is_required(self):
        self.assert_required_attr('name')

    def test_email_is_required(self):
        self.assert_required_attr('email')

    def test_sell_amount_is_required(self):
        self.assert_required_attr('sell_amount')

    def test_currency_defaults_to_BTC(self):
        assert SellOrderFactory(currency=None).currency == u'BTC'

    def test_bank_account_is_required(self):
        self.assert_required_attr('bank_account')

    def test_deposit_address_is_required(self):
        self.assert_required_attr('deposit_address')

    def test_ordered_at_defaults_to_a_datetime(self):
        assert isinstance(
            SellOrderFactory(ordered_at=None).ordered_at,
            datetime
        )
