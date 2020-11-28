import collections
        
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    """
        this is my solution for the problem which is more efficient
    """    

    def mySolution(self, nums):
        dict_value = {}
        values = list(set(nums))
        for num in values:
            value = nums.count(num)
            dict_value[num] = value
        maxValue = max(dict_value, key = dict_value.get)
        return maxValue
        
if __name__ == '__main__':
    
    sol = Solution()
    nums = [1,2,2,3,4]
    result = sol.mySolution(nums)
    print(result)