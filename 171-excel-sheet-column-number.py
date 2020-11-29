class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for letter in s:
            result = result * 26 + (ord(letter) - ord("A") + 1)
        return result
    
if __name__ == '__main__':
    
    sol = Solution()
    s = "ZY"
    result = sol.titleToNumber(s)
    print(result)