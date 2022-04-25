from collections import Counter

def spliter(tosplit):
    tosplit = list(map(int,tosplit.split()))
    return tosplit

lst = []
x, y = int(input()), Counter(list(map(int,input().split()))) #10, 2 3 4 5 6 8 7 6 5 18

for i in range(int(input())): # 6
    i = spliter(input())  # 6 55, 6 45, 6 55, 4 40, 18 60, 10 50
    if y[i[0]] == 0:
        continue
    else:
        y[i[0]] = y[i[0]] - 1
        lst.append(i[1])

print(sum(lst)) # 200