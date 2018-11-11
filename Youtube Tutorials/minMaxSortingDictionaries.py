stocks = {
    'GOOGL': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

print('Min', min(zip(stocks.values(), stocks.keys())))

print('Max', max(zip(stocks.values(), stocks.keys())))

print('Sorted', sorted(zip(stocks.values(), stocks.keys())))
print('Alphabetical', sorted(zip(stocks.keys(), stocks.values())))