board = [0]*9
game_is_over = False

player_one = 'x'
player_two = 'o'

def board_print():
    print [board[0],board[1],board[2]]
    print [board[3],board[4],board[5]]
    print [board[6],board[7],board[8]]

def winner_check():
    if board[0] == board[1] == board[2] == 'x':
        print 'Player x wins!'
        return True
    elif board[3] == board[4] == board[5] == 'x':
        print 'Player x wins!'
        return True
    elif board[6] == board[7] == board[8] == 'x':
        print 'Player x wins!'
        return True
    elif board[0] == board[3] == board[6] == 'x':
        print 'Player x wins!'
        return True
    elif board[1] == board[4] == board[7] == 'x':
        print 'Player x wins!'
        return True
    elif board[2] == board[5] == board[8] == 'x':
        print 'Player x wins!'
        return True
    elif board[0] == board[4] == board[8] == 'x':
        print 'Player x wins!'
        return True
    elif board[2] == board[4] == board[6] == 'x':
        print 'Player x wins!'
        return True
    elif board[0] == board[1] == board[2] == 'o':
        print 'Player o wins!'
        return True
    elif board[3] == board[4] == board[5] == 'o':
        print 'Player o wins!'
        return True
    elif board[6] == board[7] == board[8] == 'o':
        print 'Player o wins!'
        return True
    elif board[0] == board[3] == board[6] == 'o':
        print 'Player o wins!'
        return True
    elif board[1] == board[4] == board[7] == 'o':
        print 'Player o wins!'
        return True
    elif board[2] == board[5] == board[8] == 'o':
        print 'Player o wins!'
        return True
    elif board[0] == board[4] == board[8] == 'o':
        print 'Player o wins!'
        return True
    elif board[2] == board[4] == board[6] == 'o':
        print 'Player o wins!'
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

def player_turn(player):
    moves = input("Player {}, indicate your position using an index number.".format(player))
    while moves not in range(9):
        moves = input("Choose an integer from 0 to 8.")
    if board[moves] != 0:
        moves = input("Space is already taken; choose another.")
    board[moves] = player
    turn_end()

while not game_is_over:
    player_turn(player_one)
    if game_is_over:
        break
    player_turn(player_two)


