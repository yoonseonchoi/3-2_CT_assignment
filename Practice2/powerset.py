def powerSetRecursive(A):
    if not A:
        return [[]]
    else:
        sets = powerSetRecursive(A[:-1])
        newSets = []
        for curr in sets:
            new = curr.copy()
            new.append(A[-1])
            newSets.append(new)
        sets.extend(newSets)
        return sets

def powerSetIterative(A):
    sets = [[]]
    for n in A:
        newSets = []
        for curr in sets:
            new = curr.copy()
            new.append(n)
            newSets.append(new)
        sets.extend(newSets)
    return sets