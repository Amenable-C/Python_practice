# Min or Max in a List
def numMax(num_list):
    numM = int(num_list[0])
    for i in num_list:
        if int(num_list[i]) > numM:
            nunM = int(num_list[i])
    return numM

def numMin(num_list):
    numm = int(num_list[0])
    for i in num_list:
        if int(num_list[i]) < numM:
            nunm = int(num_list[i])
    return numm

num_list = []
while True:
    num = input("Put the number(-1 to quit): ")
    if num == '-1':
        break
    num_list.append(num)

while True:
    what = input("Input max or min to find the maximum or minimum value: ")
    if what == "min":
        print(min(num_list))
    elif what == "max":
        print(max(num_list))
    else:
        print("Bye")
        break
