import os
for i in range(25):
    day = i + 1
    try:
        os.mkdir(f'./Day {day}')
    except:
        pass
    with open(f'./Day {day}/input.txt', 'a+') as file:
        pass
    with open(f'./Day {day}/day{day}.py', 'a+') as file:
        pass
