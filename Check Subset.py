def issub(x):
    x = x.split()
    x = set(map(int,x))
    return x


for i in range(int(input())):
    c = input()
    a = issub(input())
    c = input()
    b = issub(input())
    print(a.issubset(b))
