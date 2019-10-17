import csv

file = open('data_finale.csv','r')
csvreader = csv.reader(file)
csvlist = list(csvreader)
i=1
container = {}


for row in csvlist:
    #container[]=[]
    print(csvlist[i])
    i+=1


#print(csvlist[2][6]+' '+csvlist[2][2])