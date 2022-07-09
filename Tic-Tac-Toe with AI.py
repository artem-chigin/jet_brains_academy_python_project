def input_initial_board_state():
    board_state = input()
    # board_state = "O_XOX___X"
    legal_values = {"X", "O", "_"}

    if len(board_state) == 9 and set(board_state).issubset(legal_values):
        board_state = board_state.replace("_", " ")
        return [list(board_state[0: 3]), list(board_state[3: 6]), list(board_state[6: 10])]
    else:
        print("Please input correct data. Like - _XOXOX__O")
        return input_initial_board_state()


def print_game_board(value):
    print("---------")
    for row in value:
        print("| " + " ".join(row) + " |")
    print("---------")


def count_moves(board):
    count_x = 0
    count_o = 0
    count_space = 0
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == "X":
                count_x += 1
            elif board[row][column] == "O":
                count_o += 1
            elif board[row][column] == " ":
                count_space += 1
    return count_x, count_o, count_space


def player_move_input(board):
    print("Enter the coordinates:")
    move = str(input()).split()
    # print(move)
    if not all(map(lambda x: True if x.isdigit() else False, move)):
        print("You should enter numbers!")
        return player_move_input(board)
    if not all(map(lambda x: True if x in {"1", "2", "3"} else False, move)):
        print("Coordinates should be from 1 to 3!")
        return player_move_input(board)

    row, column = move
    row = int(row) - 1
    column = int(column) - 1

    if board[row][column] == "X" or board[row][column] == "O":
        print("This cell is occupied! Choose another one!")
        return player_move_input(board)

    count_x, count_o, _ = count_moves(board)
    if count_x <= count_o:
        board[row][column] = "X"
    else:
        board[row][column] = "O"
    return board


def horizontal_or_vertical_result(board):
    for row in range(len(board)):
        if "".join(board[row]) == "XXX":
            return "X wins"
        elif "".join(board[row]) == "OOO":
            return "O wins"


def game_state(board):
    main_diagonal_result = []
    second_diagonal_result = []
    rotated_board = [["", "", ""], ["", "", ""], ["", "", ""]]

    for row in range(len(board)):
        for column in range(len(board[row])):

            rotated_board[row][column] = board[column][row]

            if row == column:
                main_diagonal_result.append(board[row][column])
            if row == len(board) - column - 1:
                second_diagonal_result.append(board[row][column])

    if horizontal_or_vertical_result(board) == "X wins":
        return "X wins"
    elif horizontal_or_vertical_result(board) == "O wins":
        return "O wins"

    if horizontal_or_vertical_result(rotated_board) == "X wins":
        return "X wins"
    elif horizontal_or_vertical_result(rotated_board) == "O wins":
        return "O wins"

    if "".join(main_diagonal_result) == "XXX" or "".join(second_diagonal_result) == "XXX":
        return "X wins"
    elif "".join(main_diagonal_result) == "OOO" or "".join(second_diagonal_result) == "OOO":
        return "O wins"

    _, _, space_fields_count = count_moves(board)
    if space_fields_count == 0:
        return "Draw"

    return "Game not finished"


def game(board):
    print_game_board(board)

    while game_state(board) == "Game not finished":

        print_game_board(player_move_input(board))

        print(game_state(board))


print("Enter the cells:")
game_board = input_initial_board_state()

game(game_board)
