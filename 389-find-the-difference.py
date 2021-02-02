import collections
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic_s = collections.Counter(s)
        dic_t = collections.Counter(t)
        for key, val in dic_t.items():
            if key not in dic_s or val > dic_s[key]:
                return key