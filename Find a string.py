x = input('')
y = input('')

k = 0
n = 0
nn = len(y)

while True:
    if y == x[n:nn]:
        k = k + 1
    n = n + 1
    nn = nn + 1
    if nn == len(x) + 1 :break

print(k)