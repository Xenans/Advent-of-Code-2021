import re
file = open('./Day 13/input.txt', 'r')
input = [line.strip() for line in file]
# print(input)


class Dot:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def plot(dots, width, height):
    board = ['.' * width for _ in range(height)]

    def print_board():
        for line in board:
            print(line)
    dot_count = 0
    for dot in dots:
        if board[dot.y][dot.x] != '#':
            dot_count += 1
        board[dot.y] = board[dot.y][:dot.x] + '#' + board[dot.y][dot.x + 1:]
    print_board()
    return dot_count


dots = []
folds = []

for entry in input:
    coordinates = re.match('([0-9]+),([0-9]+)', entry)
    if coordinates:
        dot = Dot(int(coordinates.group(1)), int(coordinates.group(2)))
        dots.append(dot)
    else:
        fold = re.match('fold along ([xy])=([0-9]+)', entry)
        if fold:
            folds.append((fold.group(1), int(fold.group(2))))

# print(dots)
# print(folds)

width = max([dot.x for dot in dots]) + 1
height = max([dot.y for dot in dots]) + 1

# print(width, height)

fold_count = 0
for fold in folds:
    fold_count += 1

    fold_direction = fold[0]
    fold_coordinate = fold[1]
    if fold_direction == 'x':
        for dot in dots:
            if dot.x > fold_coordinate:
                dot.x = fold_coordinate - (dot.x - fold_coordinate)
        width = fold_coordinate
    else:
        for dot in dots:
            if dot.y > fold_coordinate:
                dot.y = fold_coordinate - (dot.y - fold_coordinate)
        height = fold_coordinate
    if fold_count == 1:
        print(
            f'There are {plot(dots, width, height)} dots after a single fold')

plot(dots, width, height)
