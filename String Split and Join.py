def split_and_join(x):
    x = x.split()
    return "-".join(x)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)