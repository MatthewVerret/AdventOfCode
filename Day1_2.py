from Day1_1 import lines, increase_depth

list_sum_3 = []


for i in range(len(lines)-2):
    list_sum_3.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))

print(increase_depth(list_sum_3))
