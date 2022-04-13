s = input('')
d = list(input(''))
p = len(d)

if p < 4:
    position = int(d[0])
    character = d[2]
    print(s[:position]+character+s[position + 1:])
else:
    k = d[0:p - 2]
    position = int(''.join(k))
    character = d[-1]
    print(s[:position]+character+s[position + 1:])