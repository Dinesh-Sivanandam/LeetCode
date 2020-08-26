#The Leetcode program to reverse the given number even for negative values.

def reverse(num):

    """
    :type x: int
    :rtype: int
    """
    # Checking the condition for the value to be less than the highest value of 2**32 else give 0.
    if num >= 2**31-1 or num <= -2**31:
        return 0
    # if condition fails we are changing the value to string to reverse it.
    else:
        str_num = str(num)
        #Condition for the value to be positive.
        if num >= 0 :
            rev_st = str_num[::-1]
        #if the value is negative then we reverse the string from 1st index and we add '-' sign before.
        else:
            temp = str_num[1:] 
            temp2 = temp[::-1] 
            rev_st = "-" + temp2
        #again checking the condition it is a higher value if it is true returning 0.
        if int(rev_st) >= 2**31-1 or int(rev_st) <= -2**31:
            return 0
        #else we printing the answer in the integer format.
        else:
            return int(rev_st)
        
#getting the value and reversing it

if __name__ == "__main__":
    number = int(input("Enter the value to reverse: "))
    rev_num = reverse(number)
    print(rev_num)
