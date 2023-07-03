def twoSum(nums, key):
    visited = {}
    for num in nums:
        if k-num in visited:
            return True
        visited[num] = True
    return False

if __name__ == '__main__':
    nums = [5,3,10,12,9]
    k = 11
    print(twoSum(nums, k))