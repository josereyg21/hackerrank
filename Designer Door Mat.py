x = list(map(int,(input().split())))  # input s---->  11 33
ptrn, ptrn2 = ".|.", "WELCOME"
lst = [ptrn*i for i in range(3,x[0],2)]

print(ptrn.center(x[1],"-"))
for i in lst:
    print(i.center(x[1],"-"))
print(ptrn2.center(x[1],"-"))
for i in reversed(lst):
    print(i.center(x[1],"-"))
print(ptrn.center(x[1],"-"))

