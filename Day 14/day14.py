file = open('./Day 14/input.txt', 'r')
input = [line.strip() for line in file]
starting_polymer = input[0]

rules = {}
for line in input[2:]:
    rules[line[0:2]] = line[-1]

pair_mapping = {}
for rule in rules:
    # The rules map one pair to two
    # print(rule, rules[rule])
    pair_mapping[rule] = (rule[0] + rules[rule], rules[rule] + rule[1])
# print(pair_mapping)

# print(starting_polymer)
# print(rules)


pairs = {}
for index in range(len(starting_polymer) - 1):
    pair = starting_polymer[index: index + 2]
    pairs[pair] = pairs.get(pair, 0) + 1
print(pairs)

total_steps = 40
for step in range(total_steps):
    new_pairs = {}
    for pair in pairs:
        quantity = pairs[pair]
        new_pair1, new_pair2 = pair_mapping[pair]

        new_pairs[new_pair1] = new_pairs.get(new_pair1, 0) + quantity
        new_pairs[new_pair2] = new_pairs.get(new_pair2, 0) + quantity
    pairs = new_pairs

print(pairs)
# To count the total number of characters, you'll want to half the frequency of all the pair in your map, then add 1 for the characters at the start and end
char_frequency = {}

for pair in pairs:
    char1, char2 = pair
    quantity = pairs[pair]
    char_frequency[char1] = char_frequency.get(char1, 0) + quantity
    char_frequency[char2] = char_frequency.get(char2, 0) + quantity
start_char = starting_polymer[0]
end_char = starting_polymer[-1]
for bucket in char_frequency:
    char_frequency[bucket] = char_frequency[bucket] // 2 + \
        (bucket == start_char or bucket == end_char)

most_frequent = max(char_frequency, key=char_frequency.get)
least_frequent = min(char_frequency, key=char_frequency.get)
print(char_frequency[most_frequent] - char_frequency[least_frequent])
