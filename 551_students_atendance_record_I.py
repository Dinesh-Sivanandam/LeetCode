class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_count = 0
        for l in s:
            if l =='A':
                a_count += 1
        if 'LLL' not in s and a_count<2:
            return True
        else: 
            return False
if __name__ == '__main__':
    sol = Solution()
    print(sol.checkRecord("PPLLLAP"))