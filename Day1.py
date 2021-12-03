f = open('data_day1.txt', 'r')
cpt, lines = 0, f.readlines()

for i in range(1, len(lines)):
    if int(lines[i]) > int(lines[i - 1]):
        cpt += 1
