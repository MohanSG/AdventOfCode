report = []
unsafeReports = []
isSafe = 0
indexRemoved = 0
numberRemoved = 0

def checkSafe(report) -> bool:
        if all(report[i] <= report[i+1] for i in range(len(report) - 1)) and all(abs(report[i] - report[i+1]) >=1 for i in range(len(report) - 1)) and all(abs(report[i] - report[i+1]) <=3 for i in range(len(report) - 1)):
            return True
        elif all(report[i] >= report[i+1] for i in range(len(report) - 1)) and all(abs(report[i] - report[i+1]) >=1 for i in range(len(report) - 1)) and all(abs(report[i] - report[i+1]) <=3 for i in range(len(report) - 1)):
            return True
        else:
            return False
        
def checkProblemDampener(unsafeReport) -> bool:
        for i in range(len(unsafeReport)):
            indexRemoved = i
            numberRemoved = unsafeReport[i]
            unsafeReport.pop(i)
            
            if checkSafe(unsafeReport):
                return True
            else:
                unsafeReport.insert(indexRemoved, numberRemoved)
            
            indexRemoved = 0
            numberRemoved = 0

        return False
    

with open("./Aoc2_puzzle_input", "r") as f:
    for line in f:
        numbers = line.strip().split()
        
        for num in numbers:
            report.append(int(num))

        if checkSafe(report):
             isSafe = isSafe + 1
        elif checkProblemDampener(report):
             isSafe = isSafe + 1
        
        report = []

print("Safe:", isSafe)