#Pyhton coding for palindrome

def reverse(num):

    """
    :type x: int
    :rtype: int
    """

    str_num = str(num)
    #Condition for the value to be positive.
    if num >= 0 :
        rev_st = str_num[::-1]
        return (int(rev_st))
    #if the value is negative then we return not palindrome
    else:
        return("The number is not palindrome.")
        
        
#getting the value and reversing it and checking for palindrome

if __name__ == "__main__":
    
    number = int(input("Enter the value to reverse: "))
    rev_num = reverse(number)

    # Checking the given number and reversed number is equal
    if(rev_num == number):
        print("The given number is palindrome.")
    else:
        print("Not a palindrome.")
