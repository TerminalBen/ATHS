import csv

marg_fam={}
margem=[]
familia=[]
descricao=[]
stock = []

with open ('dados.csv') as datafile:
    csvreader = csv.reader(datafile)
    for row in csvreader:
        stock.append(row[5])
        margem.append(row[6].replace(',','.'))
        familia.append(row[2])
        descricao.append(row[1])
        marg_fam[row[6].replace(',','.')]= row[2]
    #print (marg_fam)

'''REMOVE WHITE LINES FROM CSV FILE
with open('data_finale.csv') as input, open('dados.csv', 'w') as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)
'''    

def margem_Alimentos():
    valor =0
    count =0
    for key in marg_fam:
        if (marg_fam[key] == 'Alimentos'):
            count +=1
            valor += float(key)
    print ('margem Alimentos: ')
    print(valor/count)
    
def margem_alcoolicas():
    valor =0
    count =0
    for key in marg_fam:
        if ('HIGIENE LIMPEZA' in marg_fam[key]):
            count +=1
            valor += float(key)
    print ('margem Prod. hig e limpeza: ')
    print(valor/count)

def margem_nalcoolicas():
    valor =0
    count =0
    for key in marg_fam:
        if (marg_fam[key]=='n_alcool'):
            count +=1
            valor += float(key)
    print ('margem bebidas nao alcoolicas: ')
    print(valor/count)

def margem_cosmeticos():
    valor =0
    count =0
    for key in marg_fam:
        if (marg_fam[key]=='cosmeticos'):
            count +=1
            valor += float(key)
    print ('margem cosmeticos: ')
    print(valor/count)

def margem_confeitarias():
    valor =0
    count =0
    for key in marg_fam:
        if (marg_fam[key]=='CONFEITARIAS'):
            count +=1
            valor += float(key)
    print ('margem confeitarias: ')
    print(valor/count)

def margem_diversos():
    valor =0
    count =0
    for key in marg_fam:
        if ('OUTROS' in marg_fam[key]):
            count +=1
            valor += float(key)
    print ('margem outros/diversos: ')
    print(valor/count)

def margem_especiarias():
    valor =0
    count =0
    for key in marg_fam:
        if ('ESPECIARIAS' in marg_fam[key]):
            count +=1
            valor += float(key)
    print ('margem especiarias: ')
    print(valor/count)

margem_especiarias()