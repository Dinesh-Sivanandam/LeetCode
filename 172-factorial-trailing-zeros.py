class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        count = 0
        while n != 0:
            s = s*n
            n -= 1
        s = str(s)
        for i in s[::-1]:
            if i == '0':
                count += 1
            else:
                return count
if __name__ == '__main__':
    
    sol = Solution()
    n = 7
    result = sol.trailingZeroes(n)
    print(result)