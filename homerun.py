# Will it be a homerun?
import math

U = int(input("Initial velocity of the ball (km/h)? ")) * (10 / 36)
angle = int(input("Lanuch angle? "))
sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))

a = 9.8
t =  ((U * sin) / a) * 2
dis = U * cos * t

print("The flying distance is %s meters." %dis)
if dis >= 120 :
    print("It will be a home run.")
else :
    print("It will not be a home run.")