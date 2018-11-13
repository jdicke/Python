stocks = {
    'GOOGL': 434,
    'AAPL': 325,
    'FB': 56,
    'AMZN': 623,
    'MSFT': 549,
}

print(min(stocks))

# Switches the values so that you can sort on the numbers instead of the names
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)