import numpy as np
file = open('./Day 3/input.txt', 'r')
input = [line.strip() for line in file]

threshold = len(input) / 2
digits = len(input[0])
array = [0] * digits

for number in input:
    for i, char in enumerate(number):
        array[i] += int(char)

gamma = ''
epsilon = ''
oxygen_candidates = np.array(input)
co2_candidates = np.array(input)


for i, digit in enumerate(array):
    gamma += '1' if digit > threshold else '0'
    epsilon += '1' if digit < threshold else '0'

    if len(oxygen_candidates) > 1:
        surviving_oxygen_candidates = []
        total = sum([int(candidate[i]) for candidate in oxygen_candidates])
        most_common = '1' if total >= len(oxygen_candidates)/2 else '0'

        for candidate in oxygen_candidates:
            if candidate[i] == most_common:
                surviving_oxygen_candidates.append(candidate)
        oxygen_candidates = surviving_oxygen_candidates

    if len(co2_candidates) > 1:
        surviving_co2_candidates = []
        total = sum([int(candidate[i]) for candidate in co2_candidates])
        most_common = '1' if total >= len(co2_candidates)/2 else '0'

        for candidate in co2_candidates:
            if candidate[i] != most_common:
                surviving_co2_candidates.append(candidate)
        co2_candidates = surviving_co2_candidates


print(f'Gamma is {gamma} (binary) = {int(gamma, 2)} (decimal)')
print(f'Epsilon is {epsilon} (binary) = {int(epsilon, 2)} (decimal)')
print(f'Together they make {int(gamma, 2) * int(epsilon, 2)}')
print(
    f'The oxygen generator rating is {oxygen_candidates[0]} (binary) = {int(oxygen_candidates[0], 2)} (decimal)')
print(
    f'The CO2 scrubber rating is {co2_candidates[0]} (binary) = {int(co2_candidates[0], 2)} (decimal)')

print(
    f'Together they make {int(oxygen_candidates[0], 2) * int(co2_candidates[0], 2)}')
