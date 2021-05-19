class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k >= len(s):
            return s[::-1]
        elif k <= len(s) < 2*k:
            return s[:k][::-1] + s[k:]
        else:
            for i in range(1, len(s)+1, 2*k):
                s = s[:i-1] + s[i-1:i+k-1][::-1] + s[i+k-1:]
            return s
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseStr("Dinesh",2))