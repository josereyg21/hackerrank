stng = int(input(''))
if stng % 2 == 0 and stng <= 5:
    print('Not Weird')
elif stng > 20 and stng % 2 == 0:
    print('Not Weird')
else:
    print('Weird')