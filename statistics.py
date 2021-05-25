# Statistics S/W
data = [27, 90, 30, 87, 56, 65, 92, 26, 40]
num = len(data)
menu = """Menu:
1. Score of a student
2. Highest score
3. Lowest score
4. Average score
5. Mid score
6. Quit"""
print(menu)
fix = int(input("What is the order of the student you want to know the score?"))
print(data[fix-1])

while True:
    print(menu)
    choice = input("Choice >> ")
    if choice == "1": #Score of a student
        for i in data:
            print(i, end=" ")
    elif choice == "2": # Highest score
        highest = sorted(data)[num-1]
        print(highest)
    elif choice == "3": # Lowest score
        lowest = sorted(data)[0]
        print(lowest)
    elif choice == "4": # Average score
        total = 0
        for i in data:
            total = total + i
        average = total / len(data)
        print(average)
    elif choice == "5": # Mid score
        if len(data) % 2 != 0:
            k = num // 2
            mid = sorted(data)[k]
        else:
            k = num // 2
            m = k - 1
            mid = (sorted(data)[m] + sorted(data)[k]) / 2
        print(mid)
    else: #Quit
        break