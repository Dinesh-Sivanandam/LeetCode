class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)+1):
            if i in nums:
                pass
            else:
                return i
            
            
sol = Solution()
result = sol.missingNumber([0,1])
print(result)