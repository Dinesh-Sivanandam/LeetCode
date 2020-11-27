class Solution(object):
    def convertToTitle(self, num):
        """
        :type n: int
        :rtype: str
        """
        #placing the alphabets to the list by ord and list comprehension
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        """
            while n is greater then 0
            we are appending the result by the capitals index value by getting the remainder of the given value dividing by 26
            then we are floor dividing the number by 26
            then we are reversing the value to get the correct ans
            then joining the values and returning it
        """
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)
    
if __name__ == '__main__':
    
    sol = Solution()
    result = sol.convertToTitle(100)
    print(result)