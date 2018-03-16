spam =['apples','cats','pizza','dogs']

def comma(items):
	for i in range(len(items)-2):
		print (items[i],end=' , ')
	print(items[-2]+' and '+ items[-1])
	
comma(spam)		