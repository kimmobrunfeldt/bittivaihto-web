import json

from flask import Blueprint, request

from bittivaihto.extensions import db
from bittivaihto.forms import SellOrderForm
from bittivaihto.models import SellOrder

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
    db.session.add(sell_order)
    db.session.commit()
    # Todo: return serialized sell_order
    return u'Created', 201
