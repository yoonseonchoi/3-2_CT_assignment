import sys
from typing import List

def sieveOfEratosthenes(n:int) -> List[int]:
    isPrime = [False] * 2 + [True] * (n-1)
    for x in range(2, int(n**0.5)+1):
        if isPrime[x]:
            for i in range(x**2, n+1, x):
                isPrime[i] = False
    return [i for i, b in enumerate(isPrime) if b]

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(sieveOfEratosthenes(n))
