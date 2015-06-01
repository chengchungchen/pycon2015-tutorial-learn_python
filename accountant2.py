item = input('What to buy: ')
price = input('Price: ')

print('Item: ' + item)
print('Price: ' + price)

print('{:<20}{:>5}'.format('Item', 'Price'))
print('-' * 25)
print('{:<20}{:>5}'.format(item, price))

