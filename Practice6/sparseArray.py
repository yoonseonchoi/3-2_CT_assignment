class SparseArray:
    def __init__(self, nums, size):
        self.size = size
        self.values = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.values[i] =  num
    
    def checkIndex(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Out of bounds')

    def set(self, i, val):
        self.checkIndex(i)
        if val:
            self.values[i] = val
        elif i in self.values:
            del self.values[i]

    def get(self, i):
        self.checkIndex(i)
        return self.values.get(i, 0)

if __name__ == '__main__':
    N = 1000
    input = [0]*N
    for i in range(N//100):
        input[i*100] = 1
    A = SparseArray(input, len(input))
    v = A.get(100)
    print(v)
    v = A.get(6)
    print(v)
    A.set(6,2)
    v = A.get(6)
    print(v)
    v = A.get(N)
    print(v)