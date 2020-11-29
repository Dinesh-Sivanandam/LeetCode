class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s = s[::-1]
        s = " ".join(s)
        
        return s
    
if __name__ == '__main__':
    
    sol = Solution()
    s = "I am a programmer"
    result = sol.reverseWords(s)
    print(result)