# All Prime Numbers Less Than N with importing

code = '''
def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
'''

##f = open('prime.py', 'w')
##f.write(code)
##f.close
with open('prime.py', 'w') as f:
    f.write(code)

from prime import is_prime


upper = int(input("Input a upper number: "))
print("All prime numbers less than %d: " %upper)

for n in range(2, upper+1):
    if is_prime(n):
        print("%d, " %n, end= '')
