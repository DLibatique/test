def board_print(board):
    print board[0:3]
    print board[3:6]
    print board[6:9]

def winner_check(player, board):
    wins = ((0,1,2), # top row
            (3,4,5), # middle row
            (6,7,8), # bottom row
            (0,3,6), # left column
            (1,4,7), # middle column
            (2,5,8), # right column
            (0,4,8), # left to right diagonal
            (2,4,6)) # right to left diagonal
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == player:
            return True, player
    return board.count(0) == 0, "draw"

def turn_end(player, board):
    board_print(board)
    game_is_over, winner = winner_check(player, board)
    if game_is_over:
        if winner == "draw":
            print "The game is a tie"
	else:
            print "Player {} wins!".format(winner)
    return game_is_over

def player_turn(player, board):
    moves = input("Player {}, indicate your position using an index number.".format(player))
    while moves not in range(9):
        moves = input("Choose an integer from 0 to 8.")
    if board[moves] != 0:
        moves = input("Space is already taken; choose another.")
    board[moves] = player
    return board

def main():
    board = [0]*9
    player_one = 'x'
    player_two = 'y'

    game_is_over = False
    current_player = player_one
    while not game_is_over:
        board = player_turn(current_player, board)
        game_is_over = turn_end(current_player, board)
        current_player = player_one if current_player == player_two else player_two
    
main()
