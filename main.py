pip install requests
pip install Flask
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

api_key = "9f9d3f9dabaf4f97a6558cbad4ab1088"

def convert_currency(amount, from_currency, to_currency, api_key):
    url = f"https://api.exchangeratesapi.io/v1/convert?access_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["success"]:
            return data
        else:
            return {"error": "API request unsuccessful"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/convert', methods=['GET'])
def handle_convert():
    amount = request.args.get('amount', type=float)
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')

    if not all([amount, from_currency, to_currency]):
        return jsonify({"error": "Missing required parameters"}), 400

    result = convert_currency(amount, from_currency, to_currency, api_key)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
