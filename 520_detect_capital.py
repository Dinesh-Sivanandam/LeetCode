# this code beats 99% of other codes
# python oneliner
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return True if word.isupper() or word.islower() or word.istitle() else False
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.detectCapitalUse('FlaG'))