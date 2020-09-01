#Python program to find the longest common prefix in the given list

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=[]
        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)
    
if __name__ == "__main__":

    list1=[]
    while True:
        print("Press 'q' to quit")
        value=input("Enter a word to append: ")
        if value != 'q':
            list1.append(value)
        else:
            break
    result = longestCommonPrefix(list1)
    print(result)
