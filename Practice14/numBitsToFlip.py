import sys

def numBitsToFlipXOR(a: int, b: int) -> int:
    xor = bin(a ^ b).replace('0b', '')
    cnt = 0
    for i in range(len(xor)):
        if xor[i] == '1':
            cnt += 1
    return cnt

if __name__ =='__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(numBitsToFlipXOR(a, b))

