while True:
    print ('Enter Your age')
    age = input()
    if age.isdecimal():
        break
    print('please enter  a numeber for your age.')

while True:
    print('please select a new password(letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('passwords can only have letters and numbers')
