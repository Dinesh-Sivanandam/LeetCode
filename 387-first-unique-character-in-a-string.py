import collections
class Solution():
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = collections.Counter(s)
        for i in range(len(s)):
            if l[s[i]] == 1:
                return i
        return -1
    
sol = Solution()
print(sol.firstUniqChar("loveleetcode"))
