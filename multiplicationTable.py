#Multiplication Table

for n in range(1, 10):
    for k in range(2, 10):
        print("%2s+%2s=%2s " %(k, n, k*n), end='')
    print('\n')