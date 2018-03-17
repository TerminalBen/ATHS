theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def Checkwin(board,letter):
	return((top-L[letter] == top-M[letter] and top-M[letter]==top-R[letter])
			(mid-L[letter] ==  mid-M[letter] and mid-L[letter]==mid-R[letter])
			(low-L[letter] ==  low-M[letter] and low-L[letter]==low-R[letter])
			(top-L[letter] ==  mid-L[letter] and mid-L[letter]==low-L[letter])
			(top-R[letter] ==  mid-R[letter] and mid-R[letter]==low-R[letter])
			(low-L[letter] ==  mid-M[letter] and mid-M[letter]==low-R[letter])
			(low-L[letter] ==  mid-M[letter] and mid-M[letter]==top-R[letter])
			)


def printBoard(board):
	print ( board['top-L'] + ' |' + board['top-M'] + ' |' + board['top-R'])           
	print ('--+--+--')
	print ( board['mid-L'] + ' |' + board['mid-M'] + ' |' + board['mid-R'])
	print ('--+--+--')
	print ( board['low-L'] + ' |' + board['low-M'] + ' |' + board['low-R'])
#printBoard(theBoard)	

def play():
	turn = 'X'
	for i in range(9):
		printBoard(theBoard)
		print('time to '+turn+'to play on witch position?')
		move = input()
		theBoard[move] = turn
		if turn=='X':
			turn = 'O'
		else:
			turn = 'X'	
	printBoard(theBoard)