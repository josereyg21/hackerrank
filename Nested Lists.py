lista = []
lista2 = []
lista3 = []
j = []
student1 = {}
n = 0

r = int(input())

for i in range(r):
    student = input('')
    calif = input('')
    lista.append(student)
    lista2.append(float(calif))
for d in lista:
    student1[d] = student1.get(d,lista2[n])
    n += 1


k = list(student1.values())
p = min(k)

while p in k:
    k.remove(p)

c = min(k)

pp = []

for x,y in student1.items():
    if y == c:
        pp.append(x)

pp.sort()
for t in pp:
    print(t)
