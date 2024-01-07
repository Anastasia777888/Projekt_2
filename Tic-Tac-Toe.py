"""
pprojekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Anastasija Kozlovska
email: kozlovska.st@gmail.com
discord: anastasia0163

"""

# vytvoreni hraci plochy
board = list(range(1,10))
win_coord = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))

def draw_board(play_board):
    print("-" * 13)
    for i in range(3):
        print(f"| {play_board[0 + i * 3]} | {play_board[1 + i * 3]} | {play_board[2 + i * 3]} |")
        print("-" * 13)


def player_input():
    while True:
        player_token = "X"
        player_move = input("Player" + player_token + "moves. Enter a number from 1 to 9 (q for quit): ")
        if player_move not in "123456789":
            print("Wrong number. Try again.")
            continue
        elif board[int(player_move) - 1] in "XO":
            print("This cell is occupied. Try again.")
            continue
        else:
            board[player_move - 1] = player_token
            break


def check_win(coord):
    for each in coord:
        if board[(each[0] - 1) ]

draw_board(board)