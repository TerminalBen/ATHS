#dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
	totalItems = 0
	for k,v in inventory.items():
		totalItems+= v
	print (inventory)	
	print ("total Items: " + str(totalItems))



def addToInventory(inventory, addedItems):
	for i in addedItems:
		inventory.setdefault(i,0)
		inventory[i] = inventory[i] + 1

inv = {'gold coin':42,'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv,dragonLoot)

displayInventory(inv)