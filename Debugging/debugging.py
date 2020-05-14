def boxprint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('symbol must be a char')
    if (width <= 2):
        raise Exception('width must be greater than 2')  
    if (height <= 2):
        raise Exception('height must be greater than 2')    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol+(' '*(width-2))+symbol)
    print (symbol*width)
'''
for sym,w,h in(('*',4,4),('#',20,5),('x',1,3),('%',3,3)):
    try:
        boxprint(sym,w,h)
    except Exception as err:
        print('there has been an error: '+str(err))
'''

import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('Start Program ')
def factorial(a):
    logging.debug('start of factorial '+str(a))
    f=1
    for i in range(1,a+1):
        f*=i
        logging.debug('i is '+str(i)+'f is '+str(f))
    logging.debug(' end of factorial')
    return f

print(factorial(4))
