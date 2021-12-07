f = open('data_day2.txt', 'r')
lines = f.readlines()

forward = depth = aim = 0

# Part 1
for i in lines:
    i = i.split()
    value = int(i[1])
    if i[0] == "forward":
        forward += value
    elif i[0] == "down":
        depth += value
    else:
        depth -= value


# Part 2
forward = depth = aim = 0

for i in lines:
    i = i.split()
    value = int(i[1])
    if i[0] == "up":
        aim -= value
    elif i[0] == "down":
        aim += value
    else:
        forward += value
        depth += aim * value
