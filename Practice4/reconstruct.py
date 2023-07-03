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

def printTree(root):
    if root is not None:
        printTree(root.left)
        print(root.data, end=' ')
        printTree(root.right)

def reconstructTree(preorder, inorder):
    if inorder:
        root = TreeNode(preorder.pop(0))
        root_index = inorder.index(root.data)
        root.left = reconstructTree(preorder, inorder[:root_index])
        root.right = reconstructTree(preorder, inorder[root_index+1:])
        return root

if __name__ == '__main__':
    preorder = ['a','b','d','e','c','f','g']
    inorder = ['d','b','e','a','f','c','g']
    root = reconstructTree(preorder, inorder)
    printTree(root)
    print('\n')
