# Lambda with map()
wage_list = []
while True:
    wage = int(input("What is your wage? (-1 to quit)"))
    if wage == -1:
        break
    wage_list.append(wage)
growth = float(input("What is the wage growth rate (%)? "))
after = map(lambda x: x * (100+growth)//100, wage_list)
print(list(after))


# Lambda with filter()
gpa_list = []
while True:
    gpa = float(input("Put the gpa score. (-1 to quit)"))
    if gpa == -1:
        break
    gpa_list.append(gpa)
low = float(input("Input the lower bound: "))
up = float(input("Input the upper bound: "))

bound = filter(lambda x : x > low and x < up, gpa_list)
print(list(bound))
