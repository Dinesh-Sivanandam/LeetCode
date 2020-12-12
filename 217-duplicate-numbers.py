class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new = set(nums)
        if len(new) < len(nums):
            return True
        return False

if __name__ == '__main__':
    
    sol = Solution()
    nums = [1,2,3,4]
    result = sol.containsDuplicate(nums)
    print(result)