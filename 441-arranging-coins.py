class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        num = 0
        while n > num:
            num = i
            n -= i
            i+=1
        return num