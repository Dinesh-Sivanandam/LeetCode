# this code beats 96.7% of other python codes
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Check if we have a valid input string
        if not s:
            return None
        # Remove '-' from the input string and make it uppercase
        s = s.replace("-","").upper()
        # Calculate length of input string
        n = len(s)
        # result is the variable for a list which will contain k separated string
        result = []
        # if length of input string is 1 then simply return the input string
        if n == 1 :
            return s
        # check for n % k value, if it is 0 (means that we can divide input string into k equal parts)
        # then start reformatting from the initial character in input string
        if n % k == 0:
            start = 0
        else:
            # if n % k value is more than 0 (means that we can NOT divide input string into k equal parts)
            # then start reformatting from (n % k)th character in input string
            start = n % k
        # Go over the entire string starting from `start` until end of input string in step of k
        for i in range(start, n, k):
            # Append the reformatted part into result
            result.append(s[i:(i+k)])
        # Returning the reformatted string
        if start == 0:
            return "-".join(result)
        else:
            return s[:(n % k)] + "-" + "-".join(result)
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.licenseKeyFormatting(( "2-5g-3-J"),2))