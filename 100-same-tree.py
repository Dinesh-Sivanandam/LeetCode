class Solution(object):
    #function to check same tree
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        """
        if the value of p and q is null returning true
        else if one of the values is null returning false
        else we use recurssion function to check the left and right values and return boolean value
        """
        if None == p and None == q:
            return True
        elif (None == p and None != q) or (None != p and None == q):
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
