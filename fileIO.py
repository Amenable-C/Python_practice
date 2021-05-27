#File I/O Exercises
data = "70 60 55 75 95 90 80 80 85 100"
f = open('number.txt', 'w')
f.write(data)
f.close()

f = open('number.txt')
data = f.read()
datalist = data.split()
print(datalist)
numlist = []
sum = 0
for i in datalist:
    num = int(i)
    numlist.append(num)
    sum = sum + num

print("Numbers =", numlist)
print("Average =", sum/len(numlist))
