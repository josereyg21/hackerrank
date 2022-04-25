to_print = []
to_append = []
x = input()
count = 0

for i in x:
    num_index = x.index(i,count)
    if num_index == 0:
        to_append.append(i)
    else:
        if i == to_append[0]:
            to_append.append(i)
        else:
            to_print.append(to_append)
            to_append = []
            to_append.append(i)
    count += 1
to_print.append(to_append)

tpl = ""
for i in to_print:
    tpl = tpl + f"({len(i)}, {i[0]}) "

print(tpl)