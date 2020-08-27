'''
    Declaring the list and a target value of adding the two values in the list and printing
    the index of the values
'''
#function for the solution
def solution(nums, target): #getting the values as arguments in the function
    for index in range(len(nums)): #getting the index values of the list
        if(nums[index]+nums[index+1] == target): #condition for the index values to be true
            return [index+1, index+2]
    else: #if condition fails returning target not found
        return("Target not found")

#starting the main loop here

if __name__ == "__main__":

    print("Enter the values by spaces: ")
    value = map(int, input().split()) #getting the values using map function
    values = list(value) #changing the values to the list and storing it
    target = int(input("Enter your target: "))
    answer = solution(values,target) #calculation the result by calling fuction
    print(answer)  #printing the value
