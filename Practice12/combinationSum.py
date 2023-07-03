import sys
from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    output = []
    candidates.sort()
    end = len(candidates)
    if candidates[-1] > target:
        for i in range(len(candidates)):
            if candidates[i] > target:
                end = i
                break

    def backtrack(combination, idx, diff):
        # foundSolution
        if diff == 0:
            output.append(combination[:])
            return
        tmp = -1
        # Iterate all possible candidates
        for j in range(idx, end):
            # isValid
            if candidates[j] == tmp:
                continue
            if diff < candidates[j]:
                break
            # place
            combination.append(candidates[j])
            # backtrack
            backtrack(combination, j+1, diff-candidates[j])
            # remove
            combination.pop()
            tmp = candidates[j]
    backtrack([], 0, target)
    return output

if __name__ == '__main__':
    candidates = list(map(int, sys.argv[2:]))
    target = int(sys.argv[1])
    output = combinationSum(candidates, target)
    print(output)

