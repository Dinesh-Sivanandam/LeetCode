def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()

if __name__ == "__main__":

    list1 = [2, 2, 1]
    result = singleNumber(list1)
    print(result)

