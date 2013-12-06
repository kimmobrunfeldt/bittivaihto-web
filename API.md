API Version 1
=============

    <base-url> = https://bittivaihto.fi/api/v1

[Adding parameters to request](http://stackoverflow.com/a/14551219)

Because of floating point rounding issues, smaller currency units are used
in the API:

* Cents(0.01€) are used instead of euros. For example 1€ would be 100.
* Millibitcoins(mBTC 0.001BTC) are used instead of bitcoins.

*Do not use floats, they will be cut off! All numbers used in money amounts are integers.*

Definitions
-----------

* Euro cent = 0.01 €
* mBTC = 0.001 BTC

Buy
---

Set buy order for a currency. Using this means you want to buy crypto currency
with euros.

POST <base-url>/buy

Options

    name: Name of buyer.
    mail: Mail address of buyer.
    address: BTC address of buyer.
    currency: The currency wanted to buy. Allowed values: btc
    amount: Amount of money in euro cents to spend in buying.
            Note: This value is NOT the amount of currency wanted to buy!
    max_price: Optional. Maximum price in euro cents(€) for the currency to
               be bought. For example 1€ would be 100
    expiration_time: Mandatory if `max_price` is set. If the buy order isn't
                     filled in this time, money will be returned to
                     `return_address`. Value is in seconds.
    return_address: Mandatory if `max_price` is set. Money will be returned to
                    this address if order isn't filled in `expiration_time`.


Example

    curl
    https://bittivaihto.fi/api/v1/buy/


Sell
---

Set sell order for a currency. Using this means you want to sell crypto currency
to get euros.

POST <base-url>/sell

Options

    name: Name of seller.
    mail: Mail address of seller.
    account: Bank account of seller.
    currency: The currency wanted to sell. Allowed values: btc
    amount: Amount of currency wanted to sell. For example 1000 (1BTC).
    min_price: Optional. Minimum price in euro cents(€) for the currency to
               be sold.
    expiration_time: Mandatory if `min_price` is set. If the buy order isn't
                     filled in this time, money will be returned to
                     `return_address`. Value is in seconds.
    return_address: Mandatory if `min_price` is set. Money will be returned to
                    this address if order isn't filled in `expiration_time`.


Example

    curl --data " \
        name=Kimmo Brunfeldt& \
        mail=kimmo.brunfeldt@kiraff.com& \
        account=IBAN account& \
        currency=btc& \
        amount=1000& \
        "

    <base-url>/sell

Ticker
------

Returns latest trade data about currency.
Check [Bitstamp ticker](https://www.bitstamp.net/api/ticker/).

GET <base-url>/ticker

Options

    currency: The currency to display information about

Example


    curl -i \
        -H "Accept: application/json" \
        -H "Content-Type: application/json" \
        <base-url>/ticker


