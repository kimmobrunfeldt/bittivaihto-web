# -*- coding: utf-8 -*-
from flexmock import flexmock
from pytest import raises
from wtforms.validators import Email, ValidationError

from bittivaihto.forms.sell_order_form import SellOrderForm, validate_decimal
from tests import BaseTestCase


def assert_required_field(form, fieldname):
    form[fieldname].data = None
    assert form[fieldname].validate(form) is False


def assert_optional_field(form, fieldname):
    form[fieldname].data = None
    assert form[fieldname].validate(form) is True


def assert_has_validator(field, instance):
    assert instance in [validator.__class__ for validator in field.validators]


class TestSellOrderForm(BaseTestCase):
    def setup_method(self, method):
        super(TestSellOrderForm, self).setup_method(method)
        self.sell_order_form = SellOrderForm()

    def test_name_is_required(self):
        assert_required_field(self.sell_order_form, 'name')

    def test_email_is_required(self):
        assert_required_field(self.sell_order_form, 'email')

    def test_email_has_email_validator(self):
        assert_has_validator(self.sell_order_form.email, Email)

    def test_bank_account_is_required(self):
        assert_required_field(self.sell_order_form, 'bank_account')

    def test_sell_amount_is_required(self):
        assert_required_field(self.sell_order_form, 'sell_amount')

    def test_sell_amount_uses_decimal_validation(self):
        import bittivaihto.forms.sell_order_form
        (
            flexmock(bittivaihto.forms.sell_order_form)
            .should_receive('validate_decimal')
        )
        self.sell_order_form.sell_amount.validate(self.sell_order_form)

    def test_currency_is_required(self):
        assert_required_field(self.sell_order_form, 'currency')

    def test_minimum_price_is_optional(self):
        assert_optional_field(self.sell_order_form, 'minimum_price')

    def test_minimum_price_uses_decimal_validation(self):
        import bittivaihto.forms.sell_order_form
        (
            flexmock(bittivaihto.forms.sell_order_form)
            .should_receive('validate_decimal')
        )
        self.sell_order_form.minimum_price.validate(self.sell_order_form)

    def test_maximum_time_is_optional(self):
        assert_optional_field(self.sell_order_form, 'maximum_time')

    def test_return_address_is_optional(self):
        assert_optional_field(self.sell_order_form, 'return_address')


class TestDecimalValidation(BaseTestCase):
    def get_field(self, field_data):
        class MockField(object):
            data = field_data
        return MockField()

    def test_doenst_raise_when_no_data(self):
        validate_decimal(self.get_field(u''))

    def test_doenst_raise_when_valid_decimal(self):
        validate_decimal(self.get_field(u'0.5'))

    def test_raises_validation_error_when_invalid_decimal(self):
        with raises(ValidationError):
            validate_decimal(self.get_field(u'0.asdsd'))
