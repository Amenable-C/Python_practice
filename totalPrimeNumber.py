# 백준 1978 // Prime Number
def prime(num):
    #global count
    count = 0
    for i in range(0, len(num)):
        p = int(num[i])
        if p == 2:
            count = count + 1
        else:
            for k in range(2, p):
                if (p % k == 0):
                    break
                elif k == p - 1:
                    count = count + 1
    return count

nums = input("Enter the numbers: ")
num = nums.split(", ")
print("The number of prime numbers is", prime(num))

