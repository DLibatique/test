board = [0]*9
game_is_over = False

def board_print():
	print [board[0],board[1],board[2]]
	print [board[3],board[4],board[5]]
	print [board[6],board[7],board[8]]

def winner_check():
	if board[0] == board[1] == board[2]:
		print 'Player {symbol} wins!'.format(symbol=board[0])
		return True
	elif board[3] == board[4] == board[5]:
		print 'Player {symbol} wins!'.format(symbol=board[3])
		return True
	elif board[6] == board[7] == board[8]:
		print 'Player {symbol} wins!'.format(symbol=board[6])
		return True
	elif board[0] == board[3] == board[6]:
		print 'Player {symbol} wins!'.format(symbol=board[0])
		return True
	elif board[1] == board[4] == board[7]:
		print 'Player {symbol} wins!'.format(symbol=board[1])
		return True
	elif board[2] == board[5] == board[8]:
		print 'Player {symbol} wins!'.format(symbol=board[2])
		return True
	elif board[0] == board[4] == board[8]:
		print 'Player {symbol} wins!'.format(symbol=board[0])
		return True
	elif board[2] == board[4] == board[6]:
		print 'Player {symbol} wins!'.format(symbol=board[2])
		return True
	elif board.count(0) == 0:
		print 'The game is a tie.'
		return True
	else:
		pass

def turn_end():
	board_print()
	if winner_check():
		game_is_over = True

def x_turn():
	global game_is_over
	x_moves = input("Player x, indicate your position using an index number.")
	if x_moves not in range(9):
		while True:
			x_moves = input("Choose an integer from 0 to 8.")
			if x_moves in range(9):
				break
	if board[x_moves] != 0:
		x_moves = input("Space is already taken; choose another.")
	board[x_moves] = 'x'
	turn_end()

def o_turn():
	global game_is_over
	o_moves = input("Player o, indicate your position using an index number.")
	if o_moves not in range(9):
		while True:
			o_moves = input("Choose an integer from 0 to 8.")
			if o_moves in range(9):
				break
	if board[o_moves] != 0:
		o_moves = input("Space is already taken; choose another.")
	board[o_moves] = 'o'
	turn_end()

while not game_is_over:
	x_turn()
	if game_is_over:
		break
	o_turn()


