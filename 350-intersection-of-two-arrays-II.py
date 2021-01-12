class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3 = []
        for num in nums1:
            if num in nums2:
                nums3.append(num)
                nums2.remove(num)
        return nums3