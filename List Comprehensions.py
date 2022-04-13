
x = [i for i in range(int(input())+1)]
y = [i for i in range(int(input())+1)]
z = [i for i in range(int(input())+1)]
n = int(input())

lst = [[i, j, k]
for i in x
for j in y
for k in z
if i + j + k != n]

print(lst)