"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

"""
#program to add one to the final value
#if the value greater then 10 then we take carry and add it to the near value
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    #getting the length of the list
    len_s = len(digits)
    #initializing the carry value to 1
    carry = 1
    """
    In for loop we are going to take the elements from the last value
    then incrementing the value to one
    then taking the single digit value by total % 10
    then taking the carry of the value bu totla / 10
    then we are assaigning the value to the list as the digit
    """
    for i in range(len_s - 1, -1, -1):
        total = digits[i] + carry
        digit = int(total % 10)
        carry = int(total / 10)
        digits[i] = digit
    #if the carry still continues as 1 to the last then we add 1 to the very first of the list
    if 1 == carry:
        digits.insert(0, 1)
    #returning the list
    return digits

#starting the main
if __name__ == "__main__":
    #declaring the list
    digits = [9, 9]
    #calling the function and storing the result
    result = plusOne(digits)
    #printing the result
    print(result)
