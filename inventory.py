import copy
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
    	print(str(v) + ' ' + str(k))
    	item_total += v
        
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):

	for key in addedItems:
		val = inventory.get(key,-1)

		if val != -1:
			inventory[key] = val + 1
		else:
			inventory.setdefault(key,1)
    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)