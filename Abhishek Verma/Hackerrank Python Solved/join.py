def split_and_join(line):
    k=line.split(' ')
    n='-'.join(k)
    return n

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)