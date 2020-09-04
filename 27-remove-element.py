#Removing Duplicates in the List

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
        
    count = 0
    #getting the index value by loop
    for i in range(len(nums)):
        #checking the condition wheather the value in the list is equal to value
        #if not replacing the value of the particular index to nums[count]
        #else skiping the condition and the count remains same
        if nums[i] != val :
            nums[count] = nums[i]
            count +=1
    return count

#Starting the main
if __name__ == "__main__":

    nums = [1,2,2,3,3]
    val = 2
    #calling the function and storing the result in the variable result
    result = removeElement(nums, val)
    print(result)
