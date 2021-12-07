import numpy as np
file = open('./Day 7/input.txt', 'r')
input = np.array(list(map(int, file.read().strip().split(','))))

max_position = max(input)

fuel_required = []
fuel_required_2 = []
for position in range(max_position):
    fuel_required.append(np.abs(input-position))
    fuel_required_2.append(np.abs(input-position) *
                           (np.abs(input-position) + 1) / 2)
print('The lowest cost for part one is:', min(
    [sum(cost) for cost in fuel_required]))
print('The lowest cost for part two is:', int(min(
    [sum(cost) for cost in fuel_required_2])))
