'''
Tic-tac-toe game utils.

'''


def create_empty_board():

    board = []
    for i in range(3):
        board.append([None] * 3)

    return board


def print_board(board):

    print('\n'.join([str(row) for row in board]))


def update_board(board, positionx,positiony, player):
    # TODO: modificar tablero con nuevo movimiento del jugador en posicion indicada.

    board[positiony][positionx] = str(player)


def check_for_winner(board):
    # TODO: evaluar si el jugador indicado ha ganado la partida.
    winner == False
    for i in range(len(board)):
        winner == False
        if board[i][0] == board[i][1] and board[i][2]:
            return board[i][0]

        elif board[0][i] == board[1][i] and board[2][i]:
            return board[0][i]
            
        elif board[0][0] == board [1][1] and [2][2]:
            return board[0][0]

        elif board[2][2] == board [1][1] and [0][0]:
            return board[2][2]
    return False
'''
Testing: 
'''
winner = False
board = create_empty_board()
print_board(board)

while winner == False:

    positionx = int(input("coordenada X: "))
    positiony = int(input("coordenada y: "))
    player = str(input("Jugador: "))
    update_board(board,positionx,positiony,player)
    print_board(board)
    if check_for_winner(board) != False:
        winner = True

print("el ganador es: ", check_for_winner(board))