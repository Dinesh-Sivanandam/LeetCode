class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # Initialize two pointers
        i = 0 # Pointer for g
        j = 0 # Pointer for s
        
        count = 0 # Number of content children
        
        # Sort the two arrays first
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]: # A content children
                count += 1
                i += 1
                j += 1
            else: # Current children is not content with current cookie
                j += 1
        
        return count
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.findContentChildren([1,2,3],[1,1]))