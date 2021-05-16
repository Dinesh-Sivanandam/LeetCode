class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        row_one = set('qwertyuiop')
        row_two = set('asdfghjkl')
        row_three = set('zxcvbnm')
        
        for word in words:
            one_valid = True
            two_valid = True
            three_valid = True
            for char in word:
                lowercase = char.lower()
                if lowercase not in row_one:
                    one_valid = False
                if lowercase not in row_two:
                    two_valid = False
                if lowercase not in row_three:
                    three_valid = False
            
            if one_valid or two_valid or three_valid:
                result.append(word)
        
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.findWords(["Hello","Alaska","Dad","Peace"]))