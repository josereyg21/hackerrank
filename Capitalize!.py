def solve(s):
    s = s.split(" ")
    s = [i.capitalize() for i in s]
    return " ".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
