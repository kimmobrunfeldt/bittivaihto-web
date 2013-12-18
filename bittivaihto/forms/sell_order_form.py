from wtforms import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import Email, Length


class SellOrderForm(Form):
    name = StringField(validators=[])
    email = StringField(validators=[])
    bank_account = StringField(validators=[])
    sell_amount = StringField(validators=[])
    currency = StringField(validators=[])
    minimum_price = StringField(validators=[])
    maximum_time = StringField(validators=[])
    return_address = StringField(validators=[])
