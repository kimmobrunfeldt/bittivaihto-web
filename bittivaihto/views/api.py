import json

from flask import Blueprint, request

from bittivaihto.extensions import db
from bittivaihto.forms import SellOrderForm
from bittivaihto.models import SellOrder
from bittivaihto.serializers import SellOrderSerializer

api = Blueprint('api', __name__)


@api.route('/sell-orders/', methods=['POST'])
def create_sell_order():
    if not request.data:
        return u'No data given.', 400

    form = SellOrderForm(data=json.loads(request.data))

    if not form.validate():
        return json.dumps(form.errors), 400

    sell_order = SellOrder()
    form.populate_obj(sell_order)
    # Todo remove?
    sell_order.deposit_address = u'<DUMMY_BITCOIN_ADDR>'
    db.session.add(sell_order)
    db.session.commit()
    print sell_order.deposit_address

    return SellOrderSerializer(sell_order).json, 201
