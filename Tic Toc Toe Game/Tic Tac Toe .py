import random
#  print the game board

board = [" " for x in range(9)]
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def move_player(icon):
    """
    This function used To register player move

    """
    # check icon_input
    number = 0
    if icon == "x":
        number = 1
    elif icon == "o":
        number = 2
    print(f"player {number}  will choose")

    # take position from player and append it
    choice = int(input("Enter move (1,9): ").strip())
    if board[choice-1] == " ":
        board[choice-1] = icon
    else:
        print("you should choose another index")


def is_victory(icon):
    """

    This Function To check who will win

    """

    if (board[0] == icon and board[1] == icon and board[2] == icon) or\
       (board[3] == icon and board[4] == icon and board[5] == icon) or\
       (board[6] == icon and board[7] == icon and board[8] == icon) or\
       (board[0] == icon and board[3] == icon and board[6] == icon) or\
       (board[1] == icon and board[4] == icon and board[7] == icon) or\
       (board[2] == icon and board[5] == icon and board[8] == icon) or\
       (board[2] == icon and board[4] == icon and board[6] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon):

        return True

    else:
        return False

def is_draw():
    """
    This Function used To keep game run until one user win

    """
    if " " not in board:
        return True
    else:
        return False


while True:
    # check player 1
    print_board()
    move_player('x')
    print_board()

    if is_victory('x'):
        print("Player 1 win")
        break
    elif is_draw():
        print("Game Over")
        break
    # check player 2
    move_player('o')
    if is_victory('o'):
        print_board()
        print("Player 2 is win")
        break
    elif is_draw():
        print("Game Over")
        break



















































































