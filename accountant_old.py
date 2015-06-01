def _show_items(items):  
	template  =  '{name:20}{price:>5}'  
	if not items:  
		print("No items. Use 'add' to add some!")  
		return  
	print()  
	print(template.format(name='Item',  price='Price'))  
	print('-' * 25)  
	for item in items:  
		print(template.format(
			name=item['name'],  price=item['price'],  
			))  
	print()

def add():
	items = []
	name = input('Item namd: ')
	price = input('Price: ')
	if name and price:
		items.append({
			'name': name, 'price': price,
		})
		_show_items(items)

if __name__ == '__main__':
	add()
