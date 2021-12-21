import os
for i in range(25):
    day = i + 1
    try:
        os.mkdir(f'./Day {day}')
        with open(f'./Day {day}/input.txt', 'a+') as file:
            pass
        with open(f'./Day {day}/day{day}.py', 'a+') as file:
            file.write(f"""file = open('./Day {day}/input.txt', 'r')
input = [line.strip() for line in file]""")
    except:
        pass
