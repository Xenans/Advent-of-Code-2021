file = open("./Day 1/input.txt", "r")
inputs = [int(x.strip()) for x in file]
# inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
prev = inputs[0]
count1 = 0
count2 = 0
length = len(inputs)
for i, num in enumerate(inputs):
    if (num > prev):
        count1 += 1
    # For a moving average we only need to compare the numbers that change
    if (i < length-3 and num < inputs[i+3]):
        count2 += 1
    prev = num
print(count1)  # 1715
print(count2)  # 1739
