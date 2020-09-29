#Program to find the single number in the list that is not repeated
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    """
    if the number not in new list adding the number to list
    if the same number exist removing the number in the new list
    then finally returning the value which is a single number in the list
    """
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()

#starting the main
if __name__ == "__main__":
    #declaring the value
    list1 = [2, 2, 1]
    #calling the function and storing the result
    result = singleNumber(list1)
    #printing the result
    print(result)

