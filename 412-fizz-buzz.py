class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l=[]
        
        for i in range(1,n+1):
            if i % 3 == 0 and i % 15 != 0:
                l.append("Fizz")
                continue
            if i % 5 == 0 and i % 15 != 0:
                l.append("Buzz")
                continue
            if i % (3*5) == 0:
                l.append("FizzBuzz")
                continue
            l.append(str(i))
        return l