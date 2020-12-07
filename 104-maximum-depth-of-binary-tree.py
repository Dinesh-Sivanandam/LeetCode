# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)
                
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
                
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = TreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    