import factory

from sqlalchemy_model_factory import SQLAlchemyModelFactory

from bittivaihto.models import SellOrder


class SellOrderFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = SellOrder

    name = u'Bill Bitter'
    email = factory.Sequence(
        lambda n: u'bill{0}@bittivaihto.fi'.format(n)
    )
    bank_account = u'FI2112345600000785'
    sell_amount = 500000
    currency = u'BTC'
    deposit_address = u'31uEbMgunupShBVTewXjtqbBv5MndwfXhb'
