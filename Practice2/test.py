def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)

def  pairSumSequence(n):
    sum = 0
    for i in range(n):
        sum += pairSum(i, i+1)
    return sum
def pairSum(a, b):
    return a + b

def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-1)

def isPrime(n):
    x = 2
    for x in range(2, x*x):
        if n % x == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

def powerOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        curr = 2 * powerOf2(n/2)
        print(curr)
        return curr

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def helper(i, s):
    if i >= len(s):
        return
    helper(i+1, s)
    print(s[i])
def reverse(s):
    helper(0, s)

if __name__ == '__main__':
    reverse('mouse')