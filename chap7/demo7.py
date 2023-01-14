items = ['Fruits', 'Books', 'Others']
prices = [98, 76, 65, 100, 50]

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
