# File I/O
# 적고, 읽어야 함

data = "70 60 55 75 95 90 80 80 85 100"
f = open('number.txt', 'w') #여기서부터 적는거
f.write(data)
f.close()

f = open('number.txt') #여기서부터는 읽는거
scores = f.read()
score_list = scores.split() #이거는 문자열
print(score_list)
sum = 0
num_list = []

for i in score_list:
    num = int(i)
    num_list.append(num) #이렇게 해야지 숫자로 저장되는거
    sum = sum + num

print("Numbers = ", num_list)
print("Ave = ", sum/len(num_list))
