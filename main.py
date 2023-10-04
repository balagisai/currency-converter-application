rates = {
    "AUDUSD": 0.8371,
    "CADUSD": 0.8711,
    "USDCNY": 6.1715,
    "EURUSD": 1.2315,
    "GBPUSD": 1.5683,
    "NZDUSD": 0.7750,
    "USDJPY": 119.95,
    "EURCZK": 27.6028,
    "EURDKK": 7.4405,
    "EURNOK": 8.6651,
}

# Crossvia table
crossvia = {
    "AUD": {"USD": "USD", "JPY": "USD"},
    "CAD": {"USD": "USD"},
    "CNY": {"USD": "USD"},
    "CZK": {"USD": "EUR"},
    "DKK": {"USD": "EUR"},
    "EUR": {"USD": "USD", "CZK": "USD", "DKK": "USD", "NOK": "EUR"},
    "GBP": {"USD": "USD"},
    "JPY": {"USD": "USD"},
    "NOK": {"USD": "EUR"},
    "NZD": {"USD": "USD"},
    "USD": {"EUR": "EUR", "JPY": "USD", "NOK": "EUR"},
}

# Function to perform currency conversion
def convertCurrency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return f"{to_currency} {amount:.2f}"

    if f"{from_currency}{to_currency}" in rates:
        rate = rates[f"{from_currency}{to_currency}"]
    else:
        cross_currency = crossvia[from_currency][to_currency]
        via_rate = rates[f"{from_currency}{cross_currency}"]
        to_rate = rates[f"{cross_currency}{to_currency}"]
        rate = via_rate * to_rate

    converted_amount = amount * rate
    precision = 2 if to_currency not in ("JPY",) else 0  # Handle precision rules
    formatted_amount = f"{to_currency} {converted_amount:.{precision}f}"
    return formatted_amount

# User interface
while True:
    from_currency = input("From Currency: ").upper()
    amount = float(input("Amount: "))
    to_currency = input("To Currency: ").upper()

    if f"{from_currency}{to_currency}" not in rates and f"{to_currency}{from_currency}" not in rates:
        print(f"Unable to find rate for {from_currency}/{to_currency}")
    else:
        result = convertCurrency(amount, from_currency, to_currency)
        print(f"= {result}")
