CatNames = []

while True:
	print('enter name of a cat')
	name = raw_input()
	if name == '':
		break
	CatNames = CatNames + [name]

print('the names of the cats are: \n')

for name in CatNames:
	print (' '+name)	

