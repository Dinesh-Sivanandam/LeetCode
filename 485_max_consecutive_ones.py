#This code beats 96% of other python codes
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #creating a empty list for uppending the sum og consecutive values and initializes count to 0
        l = []
        count = 0
        
        #talking the values oneby one to check it is 1 or 0
        # if it is 1 we are incrementing the count value contiuously
        #if not it loses the sequences and the count is appended and count is then set to 0
        
        for i in nums:
            if i == 1:
                count+=1
            else:
                l.append(count)
                count = i
                
        #At last if the count value will not be appended so we are appending at the last
        if count not in l:
            l.append(count)
            
        return max(l)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))