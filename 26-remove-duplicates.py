#Remove duplicates in the list

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    list1=[]
    #If the list is zero we return 0
    if len(nums)==0:
        return 0
    #Else we are goint to take eash number in the list and checking the value that is in the new list
    for num in nums:
        if num not in list1:
            list1.append(num)
    #Returning the sorted list
    return list1

#Starting the main function
if __name__ == "__main__":

    nums = [0,0,1,2,2,3]
    result = removeDuplicates(nums)
    print(result)
                
                
