class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        s=set()
        for i in nums: 
            if i not in s: 
                s.add(i)
        for i in range(1,len(nums)+1): 
            if i not in s: 
                res.append(i)
        return res
    
if __name__ == '__main__':
    sol = Solution()
    result = sol.findDisappearedNumbers([1,1])
    print(result)
    