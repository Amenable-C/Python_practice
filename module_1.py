code = '''
def greeting(name):
  print('Hello, ' + name)

person = {
  "name" : "Son",
  "age" : 29,
  "country" : "Korea"
}
'''

##f = open('mymod.py', 'w')
##f.write(code)
##f.close()
##
##f = open('mymod.py')
##data = f.read()
##print(data)

with open('mymod.py', 'w') as f:
    f.write(code) # f에 code 내용을 쓴다는 거
    f.close()
# 여기에는 바로 code가 py에서 있어서 바로 쓸 수 있는데, txt로 불러오면 바로 못 읽고, .read로 읽고 다시 써야함.

import mymod #mymod 파일 가져오기
mymod.greeting("Immortal") #mymod에 있는 greeting 함수 사용하기
mymod.greeting(mymod.person["name"])

import mymod as m
m.greeting("Amenable")
m.greeting(m.person["name"])

from mymod import greeting, person
greeting("Tom")
greeting(person["name"])
