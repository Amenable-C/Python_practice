# difference between sum
import math

crite = int(input("Input the criterion value = "))
sum_squa = 0
sum_cube = 0
n = 1

while True:
    sum_squa = sum_squa + math.pow(n, 2)
    sum_cube = sum_cube + math.pow(n, 3)
    if sum_cube - sum_squa > crite:
        print("The difference between the number is %d when n is %d." %(sum_cube - sum_squa, n))
        break
    else:
        n = n + 1