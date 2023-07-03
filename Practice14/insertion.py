def insert(n: int, m: int, i: int, j: int) -> int:
    mask = ((1<<i)-1) | (-1<<(j+1))
    return (n & mask) | (m << i)

def insert(n: int, m: int, i: int, j: int) -> int:
    allOnes = ~0
    left = allOnes << (j+1)
    right = ((1 << i) - 1)
    mask = left | right
    nCleared = n & mask
    mShifted = m << i
    return nCleared | mShifted
