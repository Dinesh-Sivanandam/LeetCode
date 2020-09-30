class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        initializing the start and end value
        while start less than end
        calculating the sum of the start and end value
        if it is equal to target it returns the index value
        else if the sum value less than target we are assaigning the start value +1
        else we assign end value as decremented by 1
        then the loop continues
        """
        start, end = 0, len(numbers)-1
        while start < end:
            curr = numbers[start] + numbers[end]
            if curr == target:
                return [start+1, end+1]
            elif curr < target:
                start +=1
            else:
                end -= 1

#starting the main
if __name__ == '__main__':

    #creating the class object
    sol = Solution()
    #initializing the values
    numbers = [2, 7, 11, 15]
    target = 18
    #callinf the function in the class and storing the result
    result = sol.twoSum(numbers, target)
    #printing the result
    print(result)
