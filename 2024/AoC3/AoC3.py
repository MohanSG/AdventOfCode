import re
first = []
second = []
total = 0
with open('2024\AoC3\AoC3_puzzle_input.txt') as f:
    for line in f:
        m = re.findall('mul\([0-9]*,[0-9]*\)', line)
        for mul in m:
            mul = mul.replace('mul(','')
            mul = mul.replace(')', '')

            s = mul.split(',')
            first.append(s[0])
            second.append(s[1])

    for index, item in enumerate(first):
       total = total + (int(first[index]) * int(second[index]))
    
    print(total)


            

        

    