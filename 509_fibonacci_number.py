class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = []
        fn = 0
        sn = 1
        th = 0
        i = 0
        
        if n <= 0:
            return 0
        
        if n == 1:
            return 1
        
        l.append(fn)
        
        while i < n:
            tn = fn+sn
            fn = sn
            sn = tn
            l.append(fn)
            i+=1
            
        return l[n-1]+l[n-2]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.fib(4))