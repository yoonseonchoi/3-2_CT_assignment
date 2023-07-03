def getBit(num: int, i: int) -> bool:
    return ((num & (1 << i)) != 0)

def setBit(num: int, i: int) -> bool:
    return num | (1 << i)

def checkBit(num: int, i: int) -> bool:
    mask = ~(1 << i)
    return num & mask

def clearBitsMSBThroughI(num: int, i: int) -> int:
    mask = (1 << i) -1
    return num & mask

def clearBitsIThrough0(num: int, i: int) -> int:
    mask = -1 << (i + 1)
    return num &  mask

def updateBit(num: int, i: int, bitIs1: bool) -> int:
    value = 1 if bitIs1 else 0
    mask = ~(1 << i)
    return (num & mask) | (value << i)
