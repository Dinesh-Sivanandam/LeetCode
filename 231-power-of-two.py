class Solution(object):
    def isPowerOfTwo(self, n):
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
            ans = 2 ** i
            i+=1
            
        if ans == n:
            return True
        return False

if __name__ == '__main__':
    
    sol = Solution()
    result = sol.isPowerOfTwo(4)
    print(result)