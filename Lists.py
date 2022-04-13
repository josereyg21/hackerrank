apd = lambda txt: lst.append(int(txt[1]))
ins = lambda txt: lst.insert(int(txt[1]),int(txt[2]))
srt = lambda txt: lst.sort()
rev = lambda txt: lst.reverse()
rem = lambda txt: lst.remove(int(txt[1]))
po = lambda txt: lst.pop()

dct = {
    "append": apd,
    "insert": ins,
    "sort": srt,
    "reverse": rev,
    "remove": rem,
    "pop": po 
}

lst = []
x = int(input())

for i in range(x):
    txt = input()
    if txt == 'print':
        print(lst)
    else:
        txt = txt.split()
        selec = dct[txt[0]]
        selec(txt)

