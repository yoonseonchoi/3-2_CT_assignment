import sys

def rob(nums):
    R = []
    if len(nums) == 1:
        return nums[-1]
    R.append(nums[0])
    R.append(max(nums[0], nums[1]))
    for i in range(2, len(nums)):
        R.append(max(R[i-1], nums[i]+R[i-2]))
    return R[-1]

if __name__ == '__main__':
    nums = sys.argv[1:]
    result = rob(nums)
    print(result)
