class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            num += 16 ** 8
            
        s = "0123456789abcdef"
        res = ""
        while(num > 0):
            res = s[num % 16] + res
            num /= 16
        return res
sol = Solution()
print(sol.toHex(10))