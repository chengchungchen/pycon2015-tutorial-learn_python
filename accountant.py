def _show_items(items):
    #template = '{name:20}{price:>5}'
    template = '{i:>3}  {name:20}{price:>5}'
    if not items:
        print("No items. Use 'add' to add some!")
        return
    print()
    print(template.format(name='Item', price='Price'))
    #print('-' * 25)
    print('-' * 30)
    for item in items:
        print(template.format(
            name=item['name'], price=item['price'],
        ))
    print()

import pathlib
def _get_save_path():
    my_path = pathlib.Path(__file__)
    return my_path.parent / 'items.json'

import json
def _load_items():
    try:
        with _get_save_path().open() as f:
            items = json.load(f)
    except FileNotFoundError:
            items = []
    return items

import click
@click.group()
def cli():
    pass

@cli.add_command
@click.command()
def add():
    #items = []
    items = _load_items()
    name = input('Item name: ')
    price = input('Price: ')
    if name and price:
        items.append({
            'name': name, 'price': price,
        })
        _show_items(items)
        _save_items(items)
 
@cli.add_command
@click.command()
def show():
    items = _load_items()
    _show_items(items)

import sys
@cli.add_command
@click.command()
@click.argument('index')
def remove(index):
    try:
        index = int(index)
    except ValueError:
        print('Need to input integer', file=sys.stderr)
        return
    items = _load_items()
    try:
        del items[index]
    except IndexError:
        print('Item {} does not exist!'.format(index),
                file=sys.stderr)
        return
    _show_items(items)
    _save_items(items)
    
def _save_items(items):
    with _get_save_path().open('w') as f:
        json.dump(items, f)

if __name__ == '__main__':
    cli()
