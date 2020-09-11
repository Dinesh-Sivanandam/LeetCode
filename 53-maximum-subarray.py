#Program to find the maximum sum of the array

def maxSubArray(A):
    """
    :type nums: List[int]
    :rtype: int
    """
    #length of the variable is stored in len_A
    len_A = len(A)
    #if the length of the variable is 1 then returning the same value
    if 1 == len_A:
        return A[0]
    """
    Else we are taking the element one by one and adding the elements
    if the value is less then zeor we are storing sum = 0
    else if sum > max we are placing max value is equal to sum
    else leaving the sum value and continue the process
    after the process returning the max value
    """
    max = None
    sum = 0
    for n in range(0, len_A):
        sum += A[n]
        if None == max or sum > max:
            max = sum
        if sum < 0:
            sum = 0
            continue

    return max

#Starting the main
if __name__ == "__main__":
    #declaring the values
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    #storing the result in the variable
    result = maxSubArray(nums)
    #printing the result
    print(result)
