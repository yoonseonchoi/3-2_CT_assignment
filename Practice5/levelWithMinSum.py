from collections import deque

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root

    def build(self, dic):
        nodes = {}
        hasRoot = False
        for key, value in dic.items():
            if key == 0:
                hasRoot = True
            nodes[key] = TreeNode(value)
        if not hasRoot:
            raise ValueError('No root')
        for key, node in nodes.items():
            if key == 0:
                self.root = node
            node.left = nodes.get(2*key+1, None)
            node.right = nodes.get(2*key+2, None)

def levelWithMinSum(node) -> int:
    if node == None:
        return 0
    level = 0
    q = deque([node])
    sum = {}
    while q:
        minSum = 0
        for _ in range(len(q)):
            temp = q.popleft()
            minSum += temp.data
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        sum[level] = minSum
        level += 1
    minLevel = min(sum, key=sum.get)
    return minLevel
    
if __name__ == '__main__':
    nodes = {0:9, 1:2, 2:3, 5:1, 6:5}
    T = Tree()
    T.build(nodes)
    result = levelWithMinSum(T.root)
    print(result)
    