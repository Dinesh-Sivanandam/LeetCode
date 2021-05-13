class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## if s is composed of n copies of substring m where n >=2
        ## In the case where n = 2, 
        ## s = m+m
        ## s+s = m+m+m+m
        ## In addition,
        ## make sure s cannot be matched in the head.
        ## make sure s cannot be matched at the tail.
        ## Chop off the first charcter of s. Call it s'
        ## Chop off the last character of s. Call it s''
        ## s' = m' + m where m' is m minus first character
        ## s'' = m + m'' where m'' is m minus last character
        ## s' + s'' = m' + m + m + m'' = m' + s + m''
        ## Note: if we just use s + s instead of s' + s'', it won't work because s is always in s + s
        return s in s[1:]+s[:-1]
        
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedSubstringPattern('abcab'))