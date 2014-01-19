import decimal

from wtforms import Form
from wtforms.fields import SelectField, StringField
from wtforms.validators import Email, DataRequired, ValidationError


class SellOrderForm(Form):
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email(254)])
    bank_account = StringField(validators=[DataRequired()])
    sell_amount = StringField(validators=[DataRequired()])
    currency = SelectField(
        choices=[(u'btc', u'BTC')],
        validators=[DataRequired()]
    )
    minimum_price = StringField(validators=[])
    maximum_time = StringField(validators=[])
    return_address = StringField(validators=[])

    def validate_sell_amount(self, field):
        validate_decimal(field)

    def validate_minimum_price(self, field):
        validate_decimal(field)

    def populate_obj(self, obj):
        super(SellOrderForm, self).populate_obj(obj)
        obj.sell_amount = decimal.Decimal(self.sell_amount.data)
        if self.minimum_price.data:
            obj.minimum_price = decimal.Decimal(self.minimum_price.data)


def validate_decimal(field):
    if field.data:
        try:
            decimal.Decimal(field.data)
        except decimal.InvalidOperation:
            raise ValidationError(u'Not a valid decimal value.')
