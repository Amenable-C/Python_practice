f = open('yesterday.txt', 'w')
lyrics = """Yesterday all my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday

Suddenly, I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly

Why she had to go?
I don't know, she wouldn't say
I said something wrong
Now I long for yesterday

Yesterday love was such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday"""

f.write(lyrics) #적는거임
f.close()

f = open('yesterday.txt') #여기서부터는 읽는거
i = 1
for line in f:
    print(i, line, end="")
    i = i + 1