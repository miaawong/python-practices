board_size = int(input("what size of game board?"))


def print_hori_line():
    print("---" * board_size)


def print_vert_line():
    print("|   " * (board_size + 1))


for i in range(board_size):
    print_hori_line()
    print_vert_line()

print_hori_line()

