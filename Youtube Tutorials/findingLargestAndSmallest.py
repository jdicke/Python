import heapq    # Helpful to find the largest and smallest and sorted

grades = [32, 43, 654, 34, 132, 66, 99, 534]

print(heapq.nlargest(3, grades))
print(heapq.nsmallest(3, grades))

# Why useful?

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOGL', 'price': 800},
    {'ticker': 'F', 'price': 54},
    {'ticker': 'MSFT', 'price': 313},
    {'ticker': 'TUNA', 'price': 69},
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))
print(heapq.nsmallest(2, stocks, key=lambda stock: stock['ticker']))