# Shift cipher

n = int(input("Shift? "))
pt = input("Input a sentence: ")
ct = ''

for i in pt:
    an = ord(i) + n
    c = chr(an)
    if c.isalpha() == False: an = ord(i) + n - 28
    ct = ct + chr(an)

print(ct)
