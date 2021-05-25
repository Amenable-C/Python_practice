# Test on Variable Scopes
x = 5
def f1():
    x = 10
    print("x indise", x)

f1()
print("x outside: ", x)

y = 'global'
z = 'global'
def f3():
    global y
    y = y * 2
    print(y)
    print(z)

f3()