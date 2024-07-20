from flask import Flask, request, jsonify
import re

app = Flask(__name__)

class Validator:
    @staticmethod
    def charatersCheck(name: str):
        if not bool(re.match(r'^[A-Za-z0-9\s]*$', name)):
            return 'Name contains non-English characters'
        return None

    @staticmethod
    def capitalizedCheck(name: str):
        if not name.istitle():
            return 'Name is not capitalized'
        return None

    @staticmethod
    def currencyCheck(currency: str):
        if currency not in ['TWD', 'USD']:
            return 'Currency format is wrong'
        return None

class FinanceInspector:
    @staticmethod
    def priceCheck(price: float):
        price = float(price)
        try:
            if price > 2000:
                return 'Price is over 2000'
            return price
        except ValueError:
            return 'Price is not a valid number'

    @staticmethod
    def twdExchanger(price: float, currency: str):
        if currency == 'USD':
            return price * 31, 'TWD'
        return price, currency

@app.route('/api/orders', methods=['POST'])
def processOrder():
    data = request.get_json()

    id = data.get('id')
    name = data.get('name')
    address = data.get('address')
    price = float(data.get('price'))
    currency = data.get('currency')

    # Charaters check
    error = Validator.charatersCheck(name)
    if error:
        return jsonify({'error': error}), 400

    # Capitalized check
    error = Validator.capitalizedCheck(name)
    if error:
        return jsonify({'error': error}), 400

    # Currency check
    error = Validator.currencyCheck(currency)
    if error:
        return jsonify({'error': error}), 400

    # Price in TWD check
    resPrice, resCurrency = FinanceInspector.twdExchanger(price, currency)

    # Price limit check
    resPriceChecker = FinanceInspector.priceCheck(resPrice)
    if isinstance(resPriceChecker, str):
        return jsonify({'error': resPriceChecker}), 400
    price = resPriceChecker

    response = {
        'id': id,
        'name': name,
        'address': address,
        'price': resPrice,
        'currency': resCurrency
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)