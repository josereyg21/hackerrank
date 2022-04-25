import numpy


the_array = []
rng = list(input())

for i in range(int(rng[0])):
    the_array.append(list((map(int, input().split()))))

print(max(numpy.min(the_array, axis = 1)))