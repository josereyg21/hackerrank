x = 0
y = 0
p = int(input(''))
for i in range(p):
    x += 1
    if y == 0:
        y = str(x)
    else:
        y = y + str(i+1)
    
print(y)
