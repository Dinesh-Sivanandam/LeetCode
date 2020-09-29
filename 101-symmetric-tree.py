class Solution(object):
    """
    This function works second after checking isSymmetric
    if the left and right is none then it returns true
    else if the left or right value is null then it return false
    else if the left val and right val are not equal then it returns false
    else at the last it undergoes futher left and right values to check the tree is mirror
       it checks the left.right value and right.left value of the tree is equal and also
       it checks left.left and right,right value is also equal
    if all are equal it returns true else it returns false
    """
    def isSymmetricHelp(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.isSymmetricHelp(left.right, right.left) and self.isSymmetricHelp(left.left, right.right)

    """
    The function to check the root is null and return true
    if the root is not null then we are calling the function with arguments of root.left and root.right
    """
    def isSymmetric(self, root):
        if root == None:    
            return True
        else:               
            return self.isSymmetricHelp(root.left, root.right)
