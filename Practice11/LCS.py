def LCS(A, B):
    n = len(A)
    m = len(B)
    x = [[0]*(m+1) for _ in range(n+1)]
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            if A[i] == B[j]:
                x[i][j] = x[i+1][j+1]+1
            else:
                x[i][j] = max(x[i+1][j], x[i][j+1])
    return x[0][0]

if __name__ == '__main__':
    A = 'THEIR'
    B = 'HABIT'
    print(LCS(A, B))