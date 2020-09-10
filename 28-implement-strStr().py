#Program to implement the strStr() function using the python
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    #if the length of the string is '0' we are returning 0
    if len(needle)==0:
        return 0
    #if the value is in our string returning the index value of the string of occurrence
    if needle in haystack:
        return haystack.index(needle)
    #if there is no occurrence then returning '-1'
    else:
        return -1

#Starting the main
if __name__ == "__main__":
    #declaring the values
    haystack = "hello"
    needle = "ll"

    #calling the function and storing the result
    result = strStr(haystack, needle)
    #printing the result
    print(result)
