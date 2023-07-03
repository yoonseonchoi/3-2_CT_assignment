def backtrack(nbrs, visited, path):
    # foundSolution
    if len(path) == len(nbrs):
        return path
    u = path[-1]
    visited.add(u)
    # Iterate all possible candidates
    for v in nbrs[u]:
        # isValid
        if v not in visited:
            # place
            path.append(v)
            # backtrack
            ans = backtrack(nbrs, visited, path)
            # remove
            if ans:
                return ans
            path.pop()
        visited.remove(u)
        return None

def itinerary(flights, start):
    visited = set()
    nbrs = {}
    for x, y in flights:
        if x in nbrs:
            nbrs[x].append(y)
        else:
            nbrs[x] = [y]
        if y not in nbrs:
            nbrs[y] = []
    return backtrack(nbrs, visited, [start])

if __name__ == '__main__':
    flights = [('SFO','HKO'), ('YYZ','SFO'), ('YUL','YYZ'), ('HKO','ORD')]
    start = 'YUL'
    res = itinerary(flights, start)
    print(res)
