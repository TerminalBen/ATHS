birthdays = {'Alice':'apr 1','Bob':'dec 12','Carol':'mar 4'}
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

def birthday(cena):
    while (True):
        print('Enter a name:')
        name = str(input())
        if name == ' ':
            for v in birthdays.items():
                print (v)
            break
        if name in birthdays.keys():
            print (name+' your birthday in on '+birthdays[name])

        else:
            print ('i have no iformation on your birthday')
            print('what is your birthday')
            day=str(input())
            birthdays[name] = day
            print ('Database updated!!')
            print(name + ' your birthday in on ' + birthdays[name])


def contachar(string):
    count ={}
    for character in string:
        count.setdefault(character, 0)
        count[character]+=1
    for key in sorted(count):
        print ("%c , %d" % (key,count[key]))




def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def totalBrought(guests,items):
    numbrought=0
    for k,v in guests.items():
        numbrought+= v.get(items,0)
    return numbrought


def totalguest(guests):
    total=0
    for k in guests:
        total+=1
    return total


#print('Number of things being brought:')
#print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
#print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
#print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))

#print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
#print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print (str(v)+' '+str(k))
        item_total+=1
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):

    for i in addedItems:
            inventory.setdefault(i, 1)
            inventory[i]=inventory[i]+1

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)


##displayInventory(inv)

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
##printPicnic(picnicItems, 20, 6)

