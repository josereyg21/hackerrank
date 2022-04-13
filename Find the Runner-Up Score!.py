dd = []
oo = []
yy = []
n = 0
m = 0
r = int(input())
j = input('')
d = ''.join(j)
for ii in d:
    n += 1
    if ii == ' ':
        dd.append(n-1)
for i in dd:
    if m == 0:
        oo.append(d[:i])
    if m == r - 2:
        oo.append(d[i+1:])
    else:
        t = d[dd[m]:dd[m+1]]
        w = t.lstrip()
        oo.append(w)
 
    m += 1

for e in oo:
    d = int(e)
    yy.append(d)

s = max(yy)
while s in yy:
    yy.remove(s)

yy.sort(reverse=True)
k = yy.pop(0)
print(k)
