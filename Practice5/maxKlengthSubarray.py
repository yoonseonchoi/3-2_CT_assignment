from collections import deque
def maxOfSubarray(lst, k):
    q = deque()
    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(lst[q[0]])
    for i in range(k, len(lst)):
        while q and q[0] <= i-k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
        print(lst[q[0]])
