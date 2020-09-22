#To find square root of the function
def Sqrt(value):
    #importhing the math module to use sqrt function
    import math
    #converting the value to int of the sqrt_value
    sqrt_value = int(math.sqrt(value))
    #returning the sqrt_value
    return sqrt_value

#starting the main

if __name__ == "__main__":
    #Getting the value frim the user
    value = int(input("Enter An integer to find the square root: "))
    #Calling the function and storing it in variable result
    result = Sqrt(value)
    #printing the result
    print("The sqrt of %d is %d"%(value,result))
