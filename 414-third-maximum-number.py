class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Set = set(nums)
        if len(Set) < 3:
            return max(Set)
        return sorted(Set)[-3]