"""
    This is a simple game called TicTacToe and must be played with 2 players
    The IDE used is PyCharm
"""
import random

board = ['k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
available = [str(num) for num in range(0, 10)]


def display_board(a, b):
    """Display the board game and the available spots"""
    print('Available    GAME BOARD\n' +
          '  Moves \n\n  ' +
          a[7] + '|' + a[8] + '|' + a[9] + '        ' + b[7] + '|' + b[8] + '|' + b[9] + '\n  ' +
          a[4] + '|' + a[5] + '|' + a[6] + '        ' + b[4] + '|' + b[5] + '|' + b[6] + '\n  ' +
          a[1] + '|' + a[2] + '|' + a[3] + '        ' + b[1] + '|' + b[2] + '|' + b[3])


def welcome():
    """A welcome message"""
    print('Welcome to Tic-Tac_toe. It is a game for two players')
    print('The first to go will be chosen randomly')


def ask_marker():
    """Ask the player for a marker"""
    marker = input("Player 1, which marker do you wanna be? X or O? ")
    while (marker.upper() != 'X') and (marker.upper() != 'O'):
        marker = input("Just X or O pls: ")
    return marker.upper()


def check_win(board, marker):
    """Return true if the player wins"""
    return ((board[1] == board[2] == board[3] == marker) or  # first horizontal
            (board[4] == board[5] == board[6] == marker) or  # second horizontal
            (board[7] == board[8] == board[9] == marker) or  # third horizontal
            (board[1] == board[4] == board[7] == marker) or  # first vertical
            (board[2] == board[5] == board[8] == marker) or  # second vertical
            (board[3] == board[6] == board[9] == marker) or  # third vertical
            (board[1] == board[5] == board[9] == marker) or  # first diagonal
            (board[3] == board[5] == board[7] == marker))  # second diagonal


def check_full(board):
    """Return true if the board is full of markers"""
    hold = 1
    for x in board:
        if x == ' ':
            hold += 1
    return hold == 1


def place_marker(board, available, marker, position):
    """Place the marker in the position into the board and clear the same position from availables"""
    board[position] = marker
    available[position] = ' '


def check_whitespace(board, position):
    """Return True if there is a white space in the position of the board"""
    return board[position] == ' '


def ask_input(board, name, marker):
    """Ask the player where he wants to place the marker in the board"""
    print('{}, type the position(1-9) for you marker({}): '.format(name, marker))
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_whitespace(board, position):
        try:
            position = int(input())
            if position <= 0 or position >= 10:
                raise Exception()
            elif board[position] != ' ':
                raise Exception()
        except:
            print("Invalid position, try again pls")
    return position


def get_random():
    """Chose randomly from Player 1 and 2"""
    get_first = random.randint(1, 2)
    if get_first == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def play_again():
    """Return true if want to play again."""
    option = " "
    option = str(input("Do you want to play again?? (Yes or No): "))
    while (option[0].upper() != 'Y') and (option[0].upper() != 'N'):
        option = str(input("Invalid option. try again(Yes or No): "))
    return option[0].upper() == 'Y'


if __name__ == '__main__':
    while True:
        welcome()

        marker_p1 = ask_marker()
        if marker_p1 == 'X':
            marker_p2 = 'O'
        else:
            marker_p2 = 'X'

        next_player = get_random()
        print('\nThe first player will be {} '.format(next_player.upper()))

        while True:
            if next_player == 'Player 1':
                display_board(available, board)
                place_marker(board, available, marker_p1, ask_input(board, next_player, marker_p1))
                print('\n' * 20)  # prints 20 lines to separate the outputs.
                if check_win(board, marker_p1):
                    print("The {} ({}) won. Congrats! ".format(next_player, marker_p1))
                    display_board(available, board)
                    break
                elif check_full(board):
                    print('There is a draw. No one won!')
                    display_board(available, board)
                    break
                next_player = 'Player 2'

            elif next_player == 'Player 2':
                display_board(available, board)
                place_marker(board, available, marker_p2, ask_input(board, next_player, marker_p2))
                print('\n' * 20)  # prints 20 lines to separate the outputs.
                if check_win(board, marker_p2):
                    print("The {} ({}) won. Congrats! ".format(next_player, marker_p2))
                    display_board(available, board)
                    break
                elif check_full(board):
                    print('There is a draw. No one won!')
                    display_board(available, board)
                    break
                next_player = 'Player 1'

        if not play_again():
            print('\n' * 20)  # prints 20 lines to separate the outputs.
            print('Thank you for playing :)')
            break
        else:
            board = ['k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            available = [str(num) for num in range(0, 10)]
            print('\n' * 20)  # prints 20 lines to separate the outputs.
