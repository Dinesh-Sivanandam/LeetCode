class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        ans = 0
        
        if n == 0:
            return False
        
        while ans < n:
            ans = 0
            ans = 3 ** i
            i+=1
            
        if ans == n:
            return True
        return False