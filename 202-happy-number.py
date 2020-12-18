class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        #running the loop until the n value is greater than 0
        while n > 1:
            #assaigning ans as 0
            ans = 0
            #reversing the number and squaring each value
            while n > 0:
                i = n % 10
                ans += i**2
                n = int(n/10)
            #assigning the ans as n for next iteration
            if ans <= 4 and ans != 1:
                    return False    
            n = ans
            #if the ans came as 1 then returning True else performin iteration
            if n == 1:
                return True
        if n == 1:
                return True
        return False

sol = Solution()
print(sol.isHappy(1111111))