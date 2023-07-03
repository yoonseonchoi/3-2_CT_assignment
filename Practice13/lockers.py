def runNLockers(n:int) -> int:
    openLocker = []
    lockers = [False]*n
    for i in range(n):
        for j in range(i, n, i+1):
            lockers[j] = not lockers[j]
    for k, locker in enumerate(lockers):
        if locker:
            openLocker.append(k+1)
    return len(openLocker)

if __name__ == '__main__':
    numLockers = runNLockers(100)
    print(numLockers)
    
