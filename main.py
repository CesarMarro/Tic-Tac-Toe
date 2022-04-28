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




def check_for_winner(board, player):
    # TODO: evaluar si el jugador indicado ha ganado la partida.
    pass


'''
Testing: 
'''

board = create_empty_board()
print_board(board)
positionx = int(input("coordenada X: "))
positiony = int(input("coordenada y: "))
player = str(input("Jugador: "))
update_board(board,positionx,positiony,player)
print_board(board)
