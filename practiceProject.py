inventory = {'rope':1,'torch':6,'goldcoin':42,'dagger':1,'arrow':12}

def display(inventory):
    total=0
    for k,v in inventory.items():
        print (str(k)+' '+str(v)+'\n')
        total+= int(v)
    print (str(total))

#display(inventory)

dragonloot=['dagger','goldcoin','ruby']
inv ={'goldcoin':42,'rope':1}

def addtoinventory(olddic,newlist):
    for i in newlist:
        olddic.setdefault(i,0)
        olddic[i]= olddic[i]+1
    return olddic

#display(inv)
inv = addtoinventory(inv,dragonloot)
display (inv)
