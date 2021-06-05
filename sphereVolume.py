# Sphere Volume using the formula and the integral
import math
r = float(input("Input the radius of a sphere = "))
v1 = (4/3) * math.pi * math.pow(r, 3)

v2 = 0
x = 0
dx = 0.0001
while x < r:
    v2 = v2 + math.pi * (r**2 - x**2) * dx
    x = x + dx

v2 = v2 * 2

print("The volume calculated with the formula = %f" %v1)
print("The volume integrated with delta of %f = %f" %(dx, v2))