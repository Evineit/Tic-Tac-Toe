cells = input("Enter cells:")
print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(*cells))


def is_possible(matrix):
    x_count = 0
    o_count = 0
    for x in matrix:
        if x == "X":
            x_count += 1
        elif x == "O":
            o_count += 1
    if abs(x_count - o_count) >= 2:
        return False
    else:
        return True


def is_finished(matrix):
    count = 0
    for x in matrix:
        if x != "_":
            count += 1
    if count < 5:
        return False
    else:
        return True


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
        if len([x for x in matrix if x == "_"]) > 1:
            return "Game not finished"
        return "Draw"
    else:
        return "{} wins".format(winner.pop())


def get_state(matrix):
    if is_possible(matrix):
        if is_finished(matrix):
            return get_winner(matrix)
        else:
            return "Game not finished"
    else:
        return "Impossible"


print(get_state(cells))
