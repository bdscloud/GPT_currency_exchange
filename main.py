# Main Program
api_key = "9f9d3f9dabaf4f97a6558cbad4ab1088"


def convert_currency(amount, from_currency, to_currency, api_key):
    url = f"https://api.exchangeratesapi.io/v1/convert?access_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

        data = response.json()
        if data["success"]:
            return data["result"]
        else:
            return "Error: API request unsuccessful"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Example usage
api_key = "your_api_key"
amount = 100
from_currency = "USD"
to_currency = "EUR"
result = convert_currency(amount, from_currency, to_currency, api_key)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")
