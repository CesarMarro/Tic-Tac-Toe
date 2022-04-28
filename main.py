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
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][2]:
            print("El ganador es: ", board[i][0])
            return True

        elif board[0][i] == board[1][i] and board[2][i]:
            print("El ganador es: ", board[0][i])
            return True
            pass
    return False
'''
Testing: 
'''
# winner = False
board = create_empty_board()
print_board(board)

while winner == False:

    positionx = int(input("coordenada X: "))
    positiony = int(input("coordenada y: "))
    player = str(input("Jugador: "))
    update_board(board,positionx,positiony,player)
    print_board(board)
    check_for_winner(board)
    winner = check_for_winner(board)
  