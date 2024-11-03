import random


def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board


def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2


def rotate_board(board):
    return [list(row) for row in zip(*board[::-1])]

def rotate_board_counter(board):
    return [list(row) for row in zip(*board)][::-1]

def slide_and_merge(row):
    new_row = [i for i in row if i != 0]
    merged_row = []
    i = 0
    while i < len(new_row):
        if i < len(new_row) - 1 and new_row[i] == new_row[i + 1]:
            merged_row.append(new_row[i] * 2)
            i += 2
        else:
            merged_row.append(new_row[i])
            i += 1
    return merged_row + [0] * (4 - len(merged_row))


def move(board, direction):
    original_board = [row[:] for row in board]

    if direction == 'up':
        board = rotate_board_counter(board)
        for i in range(4):
            board[i] = slide_and_merge(board[i])
        board = rotate_board(board)

    elif direction == 'down':
        board = rotate_board(board)
        for i in range(4):
            board[i] = slide_and_merge(board[i])
        board = rotate_board_counter(board)

    elif direction == 'left':
        for i in range(4):
            board[i] = slide_and_merge(board[i])

    elif direction == 'right':
        for i in range(4):
            board[i] = slide_and_merge(board[i][::-1])[::-1]

    if board != original_board:
        add_new_tile(board)

    return board


def check_win(board):
    for row in board:
        if 2048 in row:
            return True
    return False


def check_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
    return True


def print_board(board):
    for row in board:
        print("+----" * 4 + "+")
        print("|" + "|".join(f"{num:^4}" if num != 0 else "    " for num in row) + "|")
    print("+----" * 4 + "+")
