import re
first = []
second = []
total = 0
do = True;

with open('2024\AoC3\AoC3_puzzle_input.txt') as f:
        for line in f:
            m = re.findall('do\(\)|don\'t\(\)|mul\([0-9]*,[0-9]*\)', line)

            for mul in m:
                  if mul == "do()":
                        do = True;
                  elif mul == "don't()":
                        do = False;
                  
                  if do and 'mul' in mul:
                        print(mul)
                        mul = mul.replace('mul(','')
                        mul = mul.replace(')','')

                        s = mul.split(',')
                        first.append(s[0])
                        second.append(s[1])
            
        for index, item in enumerate(first):
                  total = total + (int(first[index]) * int(second[index]))
            
        print(total)


        

    