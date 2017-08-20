board = [0]*9
game_is_over = False

def board_print():
	print [board[0],board[1],board[2]]
	print [board[3],board[4],board[5]]
	print [board[6],board[7],board[8]]

def winner_check(player):
	global game_is_over
	if board[0] == board[1] == board[2] == player:
		print 'Player {symbol} wins!'.format(symbol=player.upper())
		game_is_over = True
	elif board[3] == board[4] == board[5] == player:
		print 'Player {symbol} wins!'.format(symbol=player.upper())
		game_is_over = True
	elif board[6] == board[7] == board[8] == player:
		print 'Player {symbol} wins!'.format(symbol=player.upper())
		game_is_over = True
	elif board[0] == board[3] == board[6] == player:
		print 'Player {symbol} wins!'.format(symbol=player.upper())
		game_is_over = True
	elif board[1] == board[4] == board[7] == player:
		print 'Player {symbol} wins!'.format(symbol=player.upper())
		game_is_over = True
	elif board[2] == board[5] == board[8] == player:
		print 'Player {symbol} wins!'.format(symbol=player.upper())
		game_is_over = True
	elif board[0] == board[4] == board[8] == player:
		print 'Player {symbol} wins!'.format(symbol=player.upper())
		game_is_over = True
	elif board[2] == board[4] == board[6] == player:
		print 'Player {symbol} wins!'.format(symbol=player.upper())
		game_is_over = True
	elif board.count(0) == 0:
		print 'The game is a tie.'
		game_is_over = True
	else:
		pass

def player_toggle(player):
	if player == 'x':
		player == 'o'
	else:
		player == 'x'

def turn_end():
	board_print()
	winner_check(player)
	player_toggle(player)

def x_turn():
	x_moves = input("Player x, indicate your position using an index number.")
	while x_moves not in range(9):
		x_moves = input("Choose an integer from 0 to 8.")
	while board[x_moves] != 0:
		x_moves = input("Space is already taken; choose another.")
	board[x_moves] = 'x'
	turn_end()

def o_turn():
	o_moves = input("Player o, indicate your position using an index number.")
	while o_moves not in range(9):
		o_moves = input("Choose an integer from 0 to 8.")
	while board[o_moves] != 0:
		o_moves = input("Space is already taken; choose another.")
	board[o_moves] = 'o'
	turn_end()

player = 'x'

while not game_is_over:
	x_turn()
	if game_is_over:
		break
	o_turn()


