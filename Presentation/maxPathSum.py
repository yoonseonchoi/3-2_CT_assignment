import sys

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

# Use recursive function
# The maximum path sum between two nodes is updated in the 'res'
# Time complexity: O(n) where n is the number of nodes
# Space complexity: O(h) where h is the height of the tree
def maxPathSum(root, res=-sys.maxsize):
    # Base case
    if root is None:
        return 0, res

    # Find the maximum path starting from the left child
    l, res = maxPathSum(root.left, res)
    # Find the maximum path starting from the right child
    r, res = maxPathSum(root.right, res)

    # All possible combination to get the optimal result
    # Node's value
    res = max(res, root.data)
    # Node's value + maximum path sum starting from its left child
    res = max(res, root.data+l)
    # Node's value + maximum path sum starting from its right child
    res = max(res, root.data+r)
    # Node's value + maximum path sum starting from its left and right child
    res = max(res, root.data+l+r)

    # Return the maximum path sum starting from the given node
    return max(root.data, root.data+max(l,r)), res

if __name__ == '__main__':
    nodes = {0:10, 1:2, 2:10, 3:20, 4:1, 6:-25, 13:3, 14:4}
    T = Tree()
    T.build(nodes)
    res = maxPathSum(T.root)[1]
    print(res)