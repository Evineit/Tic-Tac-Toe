import string


def get_if_equal(line):
    result = all(element == line[0] for element in line)
    if result and result != "_":
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
    if len(winner) == 2:
        return "Impossible"
    elif len(winner) == 0:
        if matrix.count("_") > 1:
            return "Game not finished"
        return "Draw"
    else:
        return "{} wins".format(winner.pop())


def get_state(matrix):
    if abs(matrix.count("X") - matrix.count("O")) < 2:
        if (matrix.count("X") + matrix.count("O")) > 5:
            return get_winner(matrix)
        else:
            return "Game not finished"
    else:
        return "Impossible"


cells = input("Enter cells:")
print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(*cells))
columns = [list(cells[6:9]), list(cells[3:6]), list(cells[0:3])]


def to_cell(a, b):
    return columns[a - 1][b - 1]


def print_board():
    print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(*columns[2], *columns[1], *columns[0]))


def next_move():
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
                if columns[col - 1][row - 1] == "_":
                    is_occupied = True
                    columns[col - 1][row - 1] = "X"
                    print_board()
                else:
                    print("This cell is occupied! Choose another one!")

            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


next_move()
# print(get_state(cells))
