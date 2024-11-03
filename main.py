from game_2048 import initialize_board, move, check_win, check_game_over, print_board


def main():
    board = initialize_board()
    print("Welcome to 2048! Use 'w', 's', 'a', 'd' to move tiles. Try to reach 2048!")
    print_board(board)

    while True:
        move_direction = input("Enter move (w: up, s: down, a: left, d: right): ").strip().lower()

        if move_direction in ['w', 's', 'a', 'd']:
            direction = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}[move_direction]
            board = move(board, direction)
            print_board(board)

            if check_win(board):
                print("Congratulations! You've reached 2048! You win!")
                break

            if check_game_over(board):
                print("Game over! No more moves possible.")
                break
        else:
            print("Invalid input. Please enter 'w', 's', 'a', or 'd'.")


if __name__ == "__main__":
    main()
