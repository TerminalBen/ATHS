
messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(items):
    print ("'")
    for i in range(len(items)-2):
        print(items[i]+',')
    print (items[-2]+' and '+items[-1])
    print ("' ")



comma(spam)


