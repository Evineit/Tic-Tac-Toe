import string


def get_if_equal(line):
    result = all(element == line[0] for element in line)
    if result and line[0] != "_":
        return line[0]
    return


def get_winner(matrix):
    winner = set()
    winner.add(get_if_equal(matrix[:3]))
    winner.add(get_if_equal(matrix[3:6]))
    winner.add(get_if_equal(matrix[6:9]))
    winner.add(get_if_equal(matrix[::3]))
    winner.add(get_if_equal(matrix[1::3]))
    winner.add(get_if_equal(matrix[2::3]))
    winner.add(get_if_equal(matrix[::4]))
    winner.add(get_if_equal(matrix[2:7:2]))
    winner.discard(None)
    if len(winner) == 0 and (matrix.count("X") + matrix.count("O")) == 9:
        return "Draw"
    elif len(winner) == 1:
        return "{} wins".format(winner.pop())
    else:
        return


def get_state(matrix):
    new_matrix = [elem for row in matrix for elem in row]
    if abs(new_matrix.count("X") - new_matrix.count("O")) < 2:
        if (new_matrix.count("X") + new_matrix.count("O")) >= 5:
            return get_winner(new_matrix)


def to_cell(a, b):
    return rows[a - 1][b - 1]


def print_board():
    print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(*rows[2], *rows[1], *rows[0]))


def next_move(player):
    is_occupied = False
    is_number = False
    in_range = False

    while not is_number or not is_occupied or not in_range:
        user_input = input("Enter the coordinates:")
        row, col = user_input.split(" ", 2)
        is_occupied = False
        is_number = False
        in_range = False
        if row in string.digits and col in string.digits:
            is_number = True
            row = int(row)
            col = int(col)
            if 0 < row <= 3 and 0 < col <= 3:
                in_range = True
                if rows[col - 1][row - 1] == "_":
                    is_occupied = True
                    rows[col - 1][row - 1] = player
                    print_board()
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


cells = "_" * 9
rows = [list(cells[6:9]), list(cells[3:6]), list(cells[0:3])]


def play():
    print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(*cells))
    player = "X"
    while not get_state(rows):
        next_move(player)
        player = "O" if player != "O" else "X"
    print(get_state(rows))


play()
