import sys

while True:
    print ('insert name!')
    name = input()
    if name != 'ben':
        continue
    print ('insert password')
    password = input()
    if password =='dickinson':
        break
print('access granted.')
sys.exit()