Trigger  = ['NOUN','ADJECTIVE','VERB']
userinput=[]

file= open('teste.txt','r')
data = file.read()

for w in data.split():
    if (w in Trigger):
        #w = w.replace(input('please insert a '+w+'\n'))
        user = input('please insert a '+w+'\n')
        userinput.append(str(user))

for word in data():
    if (word in Trigger):
        word = word.replace()

print(userinput)

