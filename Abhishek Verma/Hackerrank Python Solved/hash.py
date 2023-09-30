if __name__ == '__main__':

    n = int(input())
    Tuple1 = map(int, input().split())
    print(Tuple1)

    t = tuple(Tuple1)
    print(t)

    print(hash(t))