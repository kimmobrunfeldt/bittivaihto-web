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
    email: Mail address of seller.
    bank_account: Bank account of seller.
    currency: The currency wanted to sell. Allowed values: btc
    sell_amount: Amount of currency wanted to sell. Set as a string, e.g. "1.1"
    minimum_price: Optional. Minimum price in euros for the currency to
               be sold.
    maximum_time: Mandatory if `minimum_price` is set. If the buy order isn't
                     filled in this time, money will be returned to
                     `return_address`. Value is in seconds.
    return_address: Mandatory if `minimum_price` is set. Money will be returned to
                    this address if order isn't filled in `maximum_time`.


Validations:

    name: String. Length: 4-100. Must contain first and last name
    email: String. Max length 254. Validation is done by sending mail. But lightweight
           front-end validation is still needed.
    bank_account: String. Must be Finnish account. Finnish IBAN is 18 characters.
                  http://fi.wikipedia.org/wiki/IBAN
                  Validate: http://tarkistusmerkit.teppovuori.fi/tarkmerk.htm#iban
    currency: String. Must be in ['btc']
    sell_amount: Decimal.
                 Test if precision is too high: Max length after decimal point is 8.
                 Must be >= 0.02

    --- Following arguments are optional, check the dependencies from above ---

    minimum_price: Decimal. Test if precision is too high: max length after decimal point is 2.
                   0 < minimum_price < btc_price * 3
                   btc_price * 3 tries to limit people from doing "impossible"
                   sells. All sells that are not likely to be done might cause
                   a return. That is costly to us because of bitcoin transaction
                   fees and should be avoided.
                   Setting 0 means the same as minimum_price is None
    maximum_time: Integer. 3600 * 4 < maximum_time < 3600 * 24 * 60
                  From 4 hours to 60 days
    return_address: String. Bitcoinaddress. http://rosettacode.org/wiki/Bitcoin/address_validation
                    Note: bitcoinaddress length may vary!
                    http://bitcoin.stackexchange.com/questions/2564/how-to-validate-a-bitcoin-address-is-a-real-one

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


