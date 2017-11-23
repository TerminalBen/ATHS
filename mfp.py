def collatz(number):
    if number % 2 == 0:
        print (number//2)
        return  number // 2
    else :
        print (number//2)
        return  3*number+1


print ("give me a number")
number = input(int)

while number != 1:
    number = collatz(int (number))