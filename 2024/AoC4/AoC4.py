x = []
total = 0
up = ''
down = ''

with open('2024/AoC4/AoC4_puzzle_input.txt') as f:
    for line in f:
        x.append(line.rstrip())

    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 'X':
                    if i < len(x) - 3:
                        down = x[i][j] + x[i+1][j] + x[i+2][j] + x[i+3][j]
                    if i == 0:
                        up = x[i][j] + x[i-1][j] + x[i-2][j] + x[i-3][j]
                        
                    if down == "XMAS" or up == "XMAS":
                        total = total + 1
    
    print (total)

#The answer is too high, have another look