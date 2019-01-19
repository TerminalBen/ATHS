Trigger  = ['NOUN','ADJECTIVE','VERB']


#read file
file= open('teste.txt','r')
data = file.read()
#replace triggers in data for user input 
for w in data.split():
        if w in Trigger:
                user = str(input('insert a'+w+' !'))
                data = data.replace (w,user)

#write data to file
file = open('teste.txt','w')
file = file.write(data) 
print(file)    
