from random import randint
from time import time
from colorama import Fore
game_board = [['_', '_', '_'],
              ['_', '_', '_'],
              ['_', '_', '_']]
def display_game_board():
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == 'O':
                print(Fore.CYAN + 'O', end=' ')
            elif game_board[i][j] == 'X':
                print(Fore.MAGENTA + 'X', end=' ')
            else:
                print(Fore.GREEN + '_', end=' ')
        print(Fore.RESET)
def menu():
    choice = int(input('Please select one: \n\n1.Player vs Computer\n\n2.Player 1 vs Player 2\n\n3.Quit Game\n\n'))
    while choice < 1 or choice > 3:
        choice = int(input('Please Enter your Numbers: \n\n1.Player vs Computer\n\n2.Player 1 vs Player 2\n\n3.Quit Game\n\n'))
    return choice
def compute_game_time(start_time):
    return time() - start_time
def get_move_players(player_id, move_symbol):
    while True:
        print(player_id)
        row, col = int(input('row: ')), int(input('col: '))
        if row in range(0, 3) and col in range(0, 3):
            if game_board[row][col] == '_':
                game_board[row][col] = move_symbol
                break
            else:
                print('Unfortunately, this part of the cell is not empty.')
        else:
            print('Make sure the row or column you want is invalid. ')
def get_move_computer(name, move_symbol):
    while True:
        print(name)
        row, col = randint(0, 2), randint(0, 2)
        if game_board[row][col] == '_':
            game_board[row][col] = move_symbol
            break
        else:
            print('hey computer, bring your i7 back home cuz you did choose a filled cell!xD')
def player1_v_player2():
    start_time = time()
    while True:
        get_move_players('Player 1: ', 'X')
        display_game_board()
        if check_win() == 'X':
            print('Winner is Player1.')
            break
        get_move_players('Player 2: ', 'O')
        display_game_board()
        if check_win() == 'O':
            print('Winner is Player2.')
            break
        if check_tie():
            print('Tied!')
            break
    print('Race time: ', compute_game_time(start_time))
def player_v_computer():
    start_time = time()
    while True:
        get_move_players('Player : ', 'X')
        display_game_board()
        if check_win() == 'X':
            print('Winner is Player.')
            break
        get_move_computer('Computer: ', 'O')
        display_game_board()
        if check_win() == 'O':
            print('Winner is Computer.')
            break
        if check_tie():
            print('Tied!')
            break
    print('Race time: ', compute_game_time(start_time))
def check_win():
    winner = None
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2]:
            winner = game_board[i][0]
    for i in range(3):
        if game_board[0][i] == game_board[1][i] == game_board[2][i]:
            winner = game_board[0][i]
    if game_board[0][0] == game_board[1][1] == game_board[2][2]:
        winner = game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0]:
        winner = game_board[0][2]
    return str(winner)
def check_tie():
    if '_' in [i for j in game_board for i in j]:
        return False
    else:
        return True
def program():
    choice = menu()
    if choice == 1:
        player_v_computer()
    elif choice == 2:
        player1_v_player2()
    else:
        exit()
if __name__ == '__main__':
    program()