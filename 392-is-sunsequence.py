class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        ns = len(s)
        nt = len(t)
        j = 0  # j is pointer for s
        for i in range(nt):  # i is pointer for t
            if j == ns:
                return True
            if t[i] == s[j]:
                j += 1
        return j == ns