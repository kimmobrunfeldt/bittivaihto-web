API Version 1
=============

    <base-url> = https://bittivaihto.fi/api/v1

[Adding parameters to request](http://stackoverflow.com/a/14551219)

Because of floating point rounding issues, strings are used to pass currency units to API. For example:

    * 1.32 BTC = `'1.32'`
    * 4.01 € = `'4.01'`

If the number is too accurate, decimals will be cut off, for example:

    * `'1.0146'` in euros will be parsed to `1.01 €`
    * `'0.000000012'`in bitcoins will be parsed to `0.00000001 BTC`

**Do not use floats, they are not suitable for handling money! All numbers used in money amounts are passed as strings.**


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
    amount: Amount of money in euro to spend in buying.
            Note: This value is NOT the amount of currency wanted to buy!
    max_price: Optional. Maximum price in euros for the currency to
               be bought. Send as string!
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
    amount: Amount of currency wanted to sell. Set as a string, e.g. "1.1"
    min_price: Optional. Minimum price in euros for the currency to
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
        amount=1.1& \
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


