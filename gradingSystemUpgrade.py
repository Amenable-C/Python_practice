# Grading System Upgrade
def highest(scores):
    dis = len(scores)-1
    highest = scores[0]
    for i in range(0, dis-1):
        if scores[i] < scores[i+1]:
            highest = scores[i+1]
    return highest

def lowest(scores):
    dis = len(scores)-1
    lowest = scores[0]
    for i in range(0, dis-1):
        if scores[i] > scores[i+1]:
            lowest = scores[i+1]
    return lowest


def average(scores):
    dis = len(scores)-1
    total = 0
    for i in scores:
        total = total + i
    ave = total // dis
    return ave

scores = [0,]
while True:
    score = int(input("Enter a score(-1 to quit): "))
    if score == -1:
        break
    scores[0:0] = [score]
print(scores[-1])
print("The highest score: ", highest(scores))
print("The lowest scores: ", lowest(scores))
print("The average: ", average(scores))



