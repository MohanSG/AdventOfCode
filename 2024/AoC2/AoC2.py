report = []
isSafe = 0

def checkSafe(report) -> bool:
        if all(report[i] <= report[i+1] for i in range(len(report) - 1)) and all(abs(report[i] - report[i+1]) >=1 for i in range(len(report) - 1)) and all(abs(report[i] - report[i+1]) <=3 for i in range(len(report) - 1)):
            return True
        elif all(report[i] >= report[i+1] for i in range(len(report) - 1)) and all(abs(report[i] - report[i+1]) >=1 for i in range(len(report) - 1)) and all(abs(report[i] - report[i+1]) <=3 for i in range(len(report) - 1)):
            return True
        else:
            return False
    

with open("./Aoc2_puzzle_input", "r") as f:
    for line in f:
        numbers = line.strip().split()
        
        for num in numbers:
            report.append(int(num))

        if checkSafe(report):
             isSafe = isSafe + 1
        
        report = []

print("Safe:", isSafe)