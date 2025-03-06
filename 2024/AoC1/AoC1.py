f = open("./AoC1_puzzle_input", "r")

firstCol = []
secondCol = []
distances = 0

for line in f:
    firstCol.append(int(line[0:5]))
    secondCol.append(int(line[8:13]))

firstCol.sort()
secondCol.sort()

for x in range(1000):
    if firstCol[x] > secondCol[x]:
        distances = distances + (firstCol[x] - secondCol[x])
    elif secondCol[x] > firstCol[x]:
        distances = distances + (secondCol[x] - firstCol[x])

print("The total distance is", distances)