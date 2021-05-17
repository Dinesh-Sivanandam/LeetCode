import numpy as np
class Solution():
    def base7(self,num):
        return np.base_repr(num, base=7)

if __name__ == '__main__':
    sol = Solution()
    print(sol.base7(100))