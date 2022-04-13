
def alphanum(x):
    d = []
    for i in x:
        if i.isalnum():
            d.append(True)
        else:
            d.append(False)
    if True in d:
        print(True)
    else:
        print(False)
        
def alpha(x):
    d = []
    for i in x:
        if i.isalpha():
            d.append(True)
        else:
            d.append(False)
    if True in d:
        print(True)
    else:
        print(False)

def digit(x):
    d = []
    for i in x:
        if i.isdigit():
            d.append(True)
        else:
            d.append(False)
    if True in d:
        print(True)
    else:
        print(False)

def lower(x):
    d = []
    for i in x:
        if i.islower():
            d.append(True)
        else:
            d.append(False)
    if True in d:
        print(True)
    else:
        print(False)

def upper(x):
    d = []
    for i in x:
        if i.isupper():
            d.append(True)
        else:
            d.append(False)
    if True in d:
        print(True)
    else:
        print(False)

s = input('')

alphanum(s)
alpha(s)
digit(s)
lower(s)
upper(s)

