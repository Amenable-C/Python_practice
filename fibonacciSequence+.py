# Fibonacci Sequence
def fibo(num):
    if num <= 2:
        return 1
    else:
        return(fibo(num-1) + fibo(num-2))


num = int(input("What shall be the final index of the Fibonacci sequence? "))
for i in range(1, num+1):
    print(fibo(i), end = "  ")