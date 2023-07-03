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

def countUnival(root):
    if root == None:
        return True, 0
    l_isUnival, left = countUnival(root.left)
    r_isUnival, right = countUnival(root.right)
    cnt = left + right
    isUnival  = l_isUnival and r_isUnival and (root.left==None or root.left.data==root.data) and (root.right==None or root.right.data==root.data)
    if isUnival:
        cnt += 1
    return isUnival, cnt

if __name__ == '__main__':
    dic = {0:'a', 1:'c', 2:'b', 5:'b', 6:'b', 12:'b'}
    T = Tree()
    T.build(dic)
    isUnival, nUnival = countUnival(T.root)
    print(dic)
    print(nUnival)