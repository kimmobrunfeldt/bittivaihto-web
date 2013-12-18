from marshmallow import Serializer


class SellOrderSerializer(Serializer):
    class Meta:
        fields = (
            'name',
            'email',
            'bank_account',
            'sell_amount',
            'currency',
            'deposit_address',
            'minimum_price',
            'maximum_time',
            'return_address'
        )
