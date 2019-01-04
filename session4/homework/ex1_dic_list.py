inventory = {
    'gold'     : [500],
    'pouch'    : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell','strange berry','lint']
print(inventory)
del inventory['backpack'][1]
inventory['gold'].append(50)
print(inventory)