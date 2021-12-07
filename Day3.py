f = open("data_day3.txt", "r")
lines = f.readlines()

# Algorithm
freq_binary = []
for i in range(len(lines[0])-1):
    freq_binary.append(0)

for line in lines:
    for pos in range(len(line)-1):
        if int(line[pos]) == 1:
            freq_binary[int(pos)] += 1
        else:
            freq_binary[int(pos)] -= 1

# The gamma rate
value_gamma_rate = ''.join(str(int(f > 0)) for f in freq_binary)

# The epsilon rate
value_epsilon_rate = ''.join(str(int(f < 0)) for f in freq_binary)

# Result
print(int(value_gamma_rate, 2)*int(value_epsilon_rate, 2))
