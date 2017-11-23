catnames = []

while True:
    print ('Enter the name of cat'+str(len(catnames)+1)+' or enter nothing')
    name =input()
    if name == '':
        break
    catnames = catnames+[name]
print ('the cats names are:')
for names in catnames:
    print (' '+ names)