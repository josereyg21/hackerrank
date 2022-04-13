b = []
r = int(input())
for i in range(r+1):
    j = input()
    b.append(j)

y = b.pop(r)
x = None

for d in b:
    if d.startswith(y):
        x = d.split()
        del x[0]

z = 0
for t in x:
    z = z + float(t)

print("{0:.2f}".format(z/3))