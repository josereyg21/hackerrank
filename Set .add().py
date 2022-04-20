def stamps():
    s = set()
    for i in range(int(input())):
        s.add(input())
    return s
        
    
print(len(list(stamps())))