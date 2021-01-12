class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        L,R=1,num
        while L<=R:
            mid=(L+R)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                R = mid-1
            else:
                L = mid +1
        return False