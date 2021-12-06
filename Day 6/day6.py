file = open('./Day 6/input.txt', 'r')
# input = [int(number) for number in file.read().split(',')]
input = list(map(int, file.read().split(',')))


# Naive approach that treats fish as potentially objects
state = input[:]
days_to_simulate = 18

for day in range(days_to_simulate):
    new_fish = 0
    new_eternal_fish = 0
    for i, fish in enumerate(state):
        if fish == 0:
            state[i] = 6
            new_fish += 1
        else:
            state[i] -= 1
    state.extend([8] * new_fish)

print(len(state))

# Optimized approach using a hashmap
days_to_simulate = 256

ages = {}
for i in range(9):
    ages[i] = 0
for fish in input:
    ages[fish] += 1

for day in range(days_to_simulate):
    print(ages)
    new_fish = 0
    for age in ages.keys():
        if age == 0:
            new_fish += ages[age]
        else:
            ages[age - 1] = ages[age]
    ages[6] = ages[6] + new_fish
    ages[8] = new_fish
print(sum(ages.values()))
