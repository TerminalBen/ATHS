#collatz remastered

def collatz(number):
	if number %2 ==0:
		print (number//2)
		return number // 2
	else:
		print (3*number+1)
		return 3 * number+1

print ("give me a number \n") 
try:

	inp = input(int)
	while inp!= 1:
		inp = collatz(int(inp))	

except ValueError:
	print('invalid literal for int() with base 10: 'puppy'')