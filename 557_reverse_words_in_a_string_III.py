class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        j = []
        l = list(s.split(' '))
        for w in l:
            j.append(w[::-1])
        return " ".join(j)

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("He is a Good boy"))