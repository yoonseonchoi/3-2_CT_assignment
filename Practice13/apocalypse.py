import random
import sys

def runNFamilies(n:int) -> float:
    girls = 0
    children = []
    while girls != n:
        randoms = random.randint(0, 1)
        if randoms == 1:
            children.append(1)
        else:
            girls += 1
            children.append(0)
    ratio = girls / len(children)
    return ratio

if __name__ == '__main__':
    n = int(sys.argv[1])
    r = runNFamilies(n)
    print(r)

