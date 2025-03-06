firstCol = []
secondCol = []
similarityScore = 0
multiply = 0

with open("./AoC1-2_puzzle_input", "r") as f:
    for line in f:
        first, second = line.strip().split()
        firstCol.append(int(first))
        secondCol.append(int(second))
    
    for x in firstCol:
        for i in secondCol:
            if i == x:
                multiply = multiply + 1
        
        similarityScore = similarityScore + (x * multiply)
        multiply = 0

    print(similarityScore)
