def Func(n):
    return 1 if n < 3 else Func(n-1) + Func(n-3)

if __name__ == '__main__':
    for i in range(0, 16):
        print(Func(i))