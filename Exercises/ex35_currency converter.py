# 35. Currency Converter
# Convert USD into multiple currencies using fixed exchange rates.


def currency_converter(usd, exchange_rates):
    for currency, rate in exchange_rates.items():
        print(f"+ {currency}: {usd * rate}")


exchange_rates = {
    "EUR": 0.92,   # Euro
    "GBP": 0.79,   # British Pound
    "JPY": 155.0,  # Japanese Yen
    "CAD": 1.36,   # Canadian Dollar
    "AUD": 1.50,   # Australian Dollar
    "SGD": 1.34,   # Singapore Dollar
    "CNY": 7.25,   # Chinese Yuan
    "MYR": 4.70,   # Malaysian Ringgit
    "INR": 83.0,   # Indian Rupee
    "VND": 24500.0  # Vietnamese Dong
}

usd = float(input("Enter the amount in USD: "))
currency_converter(usd, exchange_rates)
