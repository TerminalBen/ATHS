def multiply (a,b):
    return(a*b)

#print(multiply (3,4) )

def getCount(inputStr):
    num_vowels = 0
    # your code here
    v = ['a','e','i','o','u']
    for i in inputStr:
        if (i in v):
            num_vowels+=1
    return num_vowels

#print(getCount('abracadabra'))

def find_smallest_int(arr):
    return (min(arr))

def friend(x):
    f =[]
    for a in x:
        if len(a)== 4:
            f.append(a)
    return (f)
#def friend(x):
#    return [f for f in x if len(f) == 4]

#print (friend(["Ryan", "Kieran", "Mark"]))

def array_diff (arr1,arr2):
    aux = []
    for a in  arr1:
        if a not in arr2:
            aux.append(a)
    return (aux)

#print(array_diff([1,2,2,2,3],[2]))
#def array_diff(a, b):
#    return [x for x in a if x not in b]