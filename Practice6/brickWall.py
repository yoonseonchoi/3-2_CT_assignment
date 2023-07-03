from collections import defaultdict

def fewestNumber(bricks):
    hashmap = defaultdict(int)
    cnt = 0
    for row in bricks:
        sum = 0
        for i in range(len(row)-1):
            sum += row[i]
            hashmap[sum] += 1
            cnt = max(cnt, hashmap[sum])
    return len(bricks) - cnt

if __name__ == '__main__':
    bricks = [[3,5,1,1],
              [2,3,3,2],
              [5,5],
              [4,4,2],
              [1,3,3,3],
              [1,1,6,1,1]]
    n = fewestNumber(bricks)
    print(n)

