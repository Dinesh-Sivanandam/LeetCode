class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic, seen = {}, set()
        str = str.split(' ')
        if len(str) != len(pattern):
            return False
        for i in range(len(str)):
            if pattern[i] not in dic:
                if str[i] in seen:
                    return False
                dic[pattern[i]] = str[i]
                seen.add(str[i])
            else:
                if dic[pattern[i]] != str[i]:
                    return False
        return True
    
sol = Solution()
result = sol.wordPattern('abba', 'dog cat cat dog')
print(result)