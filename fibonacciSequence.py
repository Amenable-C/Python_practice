# Fibonacci Sequence
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("What shall be the final index of the Fibonacci sequence?"))
if num <= 2:
    print("Sorry, the final index must be greater than 2")
else:
    print("The Fibonacci sequence:", end="")
    for n in range(1, num+1):
        print(fibo(n), end=" ")
