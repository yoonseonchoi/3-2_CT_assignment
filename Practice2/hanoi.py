import sys

def hanoi(n: int, a=1, b=2, c=3) -> int:
    if n == 0:
        return
    elif n == 1:
        print('Move ' + str(a) + ' to ' + str(c))
        return
    else:
        hanoi(n-1, a, c, b)
        print('Move ' + str(a) + ' to ' + str(c))
        hanoi(n-1, b, a, c)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        hanoi(n)
