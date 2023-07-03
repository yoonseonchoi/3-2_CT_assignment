from typing import List

# Jump Game II
# 최대로 원소 값만큼 건너 뛸 수 있으며 마지막 원소에 도착할 때까지 jump 횟수의 최솟값
def jump(nums: List[int]) -> int:
    left, right, res = 0, 0, 0
    while right < len(nums) - 1:
        longest = 0
        for i in range(left, right + 1):
            longest = max(longest, i + nums[i])
        left = right + 1
        right = longest
        res += 1
    return res
# O(n) time
# O(1) space

# Valid Parenthesis (괄호 짝 맞추기)
# *은 '(', ')', ' ' 로 대체될 수 있음
def checkValidString(s):
    low, high = 0, 0
    for i in s:
        if i == '(':
            high += 1
            low += 1
        if i == ')':
            high -= 1
            low = max(low - 1, 0)
        if i == '*':
            high += 1
            low = max(low - 1, 0)
        if high < 0:
            return False
    return low == 0
# O(n) time
# O(1) space

# Minimum Deletion and Insetion
# x에서 y로 수정할 때 deletion과 insertion 개수의 최소값
# LCS 문제와 비슷
def minDelIns(x: str, y: str) -> int:
    X, Y, L = len(x), len(y), []
    for i in range(X+1):
        L.append([])
        for j in range(Y+1):
            L[i].append(0)
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    maxSubsequence = L[X][Y]
    deletion = X-maxSubsequence
    insertion = Y-maxSubsequence
    return deletion, insertion
# O(mn) time
# O(mn) space

# Climbing Stairs
def climbStairs(n:int) -> int:
    one, two = 1, 1
    for _ in range(n-1):
        temp = one
        one += two
        two = temp
    return one
# O(n) time
# O(1) space

# Beautiful Arrangement
class Solution:
    def beautifulArrangement(self, n):
        visited = [False]*(n+1)
        self.cnt = 0
        self.helper(n, 1, visited)
        return self.cnt
    def helper(self, n, idx, visited):
        if idx > n:
            self.cnt += 1
        for i in range(1, n+1):
            if not visited[i] and (idx%i == 0 or i%idx == 0):
                visited[i] = True
                self.helper(n, idx+1, visited)
                visited[i] = False
# O(k) time, where k is the number of valid permutations
# O(n) space

# Count total set bits in first N Natural Numbers
def countBits(n):
    res = 0
    for i in range(1, n+1):
        while i > 0:
            if i % 2 == 1:
                res += 1
            i = i // 2
    return res
# O(nlogn) time
# O(1) space

# Knapsack Problem
def knapsack(W: int, wt: List[int], val: List[int]) -> int:
    n = len(val)
    K = [[0 for _ in range(W + 1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] > w:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(K[i-1][w], K[i-1][w-wt[i-1]] + val[i-1])
    return K[n][W]
# O(nW) time
# O(nW) space

def knapsackBetter(W: int, wt: List[int], val: List[int]) -> int:
    n = len(val)
    K = [[0 for _ in range(W + 1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i%2][w] = 0
            elif wt[i-1] > w:
                K[i%2][w] = K[(i-1)%2][w]
            else:
                K[i%2][w] = max(K[(i-1)%2][w], K[(i-1)%2][w-wt[i-1]] + val[i-1])
    return K[n%2][W]
# O(nW) time
# O(2W) space