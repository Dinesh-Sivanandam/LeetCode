class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #This code beats 99% of another python submissions
        #changing the number to binary
        b_num = "{0:b}".format(num)
        #making a list for appeding the complements
        l = []
        #taking each elements for complement
        for i in b_num:
            if i == '1':
                l.append('0')
            else:
                l.append('1')
        #joining the elementswithout space
        s = ''.join(l)
        #returning the integer value for the joines value
        return int(s,2)
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.findComplement(10)) 
