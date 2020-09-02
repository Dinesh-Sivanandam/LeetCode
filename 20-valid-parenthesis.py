def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    #lists for declaring the paranthesis
    left = ['(', '{', '[']
    right = [')', '}', ']']

    #A stack for checking the parenthesis
    stack = []
    #getting the paranthesis one by one
    for letter in s:
        if letter in left:
            stack.append(letter)
        elif letter in right:
            if len(stack) <= 0:
                return False
            if left.index(stack.pop()) != right.index(letter):
                return False
    return len(stack) == 0

#Running the main function
if __name__ == "__main__":
    #getting input from the user
    string = input("Enter the paranthesis: ")

    #storing the value in the result variable
    result = isValid(string)

    #printing the result
    print(result)
