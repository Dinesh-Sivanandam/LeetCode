#finding the length of the last word in the given string
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    #length of the string is storing the len_s
    len_s = len(s)
    #if the length of the string is 0 we are returning 0
    if 0 == len_s:
        return 0
    #else we are getting the index in the index variable
    #declaring len of last word is 0 as default
    index = len_s - 1
    len_last_word = 0

    """
    if the string is like 'a b ' last as blankspace
    we are reducing the index value and doing the rest process
    """ 
    while index >= 0 and ' ' == s[index]:
        index -= 1

    """
    checking the condition index >=0 and s[index] not = ' '
    if the condition ok we are making the length +1 and index-1 for checking from last
    then at last ew are returning the len of last word
    """
    while index >= 0 and ' ' != s[index]:
        len_last_word += 1
        index -= 1
    return len_last_word

#starting the main
if __name__ == "__main__":
    #declaring the variable
    string = "Hello World"
    #calling the function and storing the result in the variable
    result = lengthOfLastWord(string)
    #printing the result
    print(result)
