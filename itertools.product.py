from itertools import product

def mix(x,y):
    m = list(product(x,y))
    return m
    

x, y = list(map(int,input().split())), list(map(int,input().split()))

for i in mix(x, y):
    print(i, end=" ")