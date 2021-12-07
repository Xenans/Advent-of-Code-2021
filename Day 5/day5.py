import re
import numpy as np
file = open('./Day 5/input.txt')
input = [line.strip() for line in file]
# print(input)

matches = [re.search('(\d+,\d+) -> (\d+,\d+)', line) for line in input]
coordinates = [([int(number) for number in match.group(1).split(',')],
                [int(number) for number in match.group(2).split(',')]) for match in matches]
# print(coordinates)

board = np.zeros((1000, 1000))
board_w_diags = np.zeros((1000, 1000))
# print(board)

for [x1, y1], [x2, y2] in coordinates:
    # print(x1, y1, x2, y2)
    if x1 == x2 or y1 == y2:
        start = (min(x1, x2), min(y1, y2))
        end = (max(x1, x2)+1, max(y1, y2)+1)
        board[start[0]: end[0], start[1]: end[1]] += 1
        board_w_diags[start[0]: end[0], start[1]: end[1]] += 1
    # Otherwise it's diagonal
    else:
        if x2 > x1 and y2 > y1:
            sign = [1, 1]
        elif x2 < x1 and y2 < y1:
            sign = [-1, -1]
        elif x1 > x2 and y2 > y1:
            sign = [1, -1]
        else:
            sign = [-1, 1]
        for i in range(abs(x2 - x1) + 1):
            board_w_diags[x1 + i * sign[1], y1 + i * sign[0]] += 1
safe_zones = board >= 2
safe_zones_diag = board_w_diags >= 2
print(safe_zones.sum())
print(safe_zones_diag.sum())
# print(safe_zones_diag.astype(int))
# print(board_w_diags.transpose().astype(int))
