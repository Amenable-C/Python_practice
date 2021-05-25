#Lambda Exercises / Program #1
wages = [3200, 4150, 3900, 3650, 4300]
rate = float(input("What is the wage growth rate(%)? "))
newWages = map(lambda x: '%0.2f' %(x * ((100+rate)/100)), wages)
print("Wages in 2022: ", list(newWages))

#Lambda Exercises / Program #2
gpa = [3.75, 4.03, 4.35, 3.28, 2.96, 3.51, 3.69]
lower = float(input("Input the lower bound: "))
upper = float(input("Input the upper bound: "))
newGpa = filter(lambda x: (x > lower and x < upper), gpa)
print("GPAs between %s and %s" %(lower, upper), list(newGpa))