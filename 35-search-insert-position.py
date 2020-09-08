#The program to find the index of inserted element in the list
def searchPosition(list1, target):
    #declaring the count variable to count the index
    count = 0
    #if the conditon where the element is equal to target we are printhing the index and breaking it
    for i in range (0, len(list1)):
        if list1[i]  == target:
            return (i)
            break
    #else we are cheching the element that is less than the value
    for j in range(0, len(list1)):
        if list1[j] <= target:
            count += 1
    return(count)

#starting the main
if __name__ == "__main__":

    #declaring the values
    list1 = [1, 3, 4, 5]
    target = 0
    #calling the function and storing it n result variable
    result = searchPosition(list1, target)
    #printing the result
    print(result)
