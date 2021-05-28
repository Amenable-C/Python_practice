codeMate = '''
def sum(a, b):
    return a + b
def diff(a, b):
    return abs(a - b)
'''

with open('sumAndDiff.py', 'w') as f:
    f.write(codeMate)


import sumAndDiff

s = input("Input two numvers: ")
nums = s.split(', ')
n1 = int(nums[0])
n2 = int(nums[1])
print("Sum =", sumAndDiff.sum(n1, n2)) # 바로 sum 쓰면 안됨. 모듈이름 먼저 적어줘야 함.
print("Diff =", sumAndDiff.diff(n1, n2))