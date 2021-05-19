class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if(len(a)!=len(b)):
            if(len(a)>len(b)):
                return len(a)
            else:
                return len(b)
        else:
            if(a==b):
                return -1
            else:
                return len(a)
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.findLUSlength('aaa','bbb'))