import sys

def bowling(nums):
    if not nums:
        return 0
    B = {}
    B[len(nums)] = 0
    B[len(nums)+1] = 0
    for i in reversed(range(1, len(nums))):
        B[len(nums)-1] = int(nums[i])
        B[i-1] = max(B[i], int(nums[i-1])+B[i], int(nums[i])*int(nums[i-1])+B[i+1])
    return B[0]

if __name__ == '__main__':
    nums = sys.argv[1:]
    print(bowling(nums))

