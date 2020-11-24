"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
            push(x) -- Push element x onto stack.
            pop() -- Removes the element on top of the stack.
            top() -- Get the top element.
            getMin() -- Retrieve the minimum element in the stack.
"""

#Code using stack
from collections import deque
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.container.append(x)

    def pop(self):
        """
        :rtype: None
        """
        return self.container.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.container[-1]

    def getMin(self):
        """
        :rtype: int
        """
        list1 = [x for x in self.container]
        return min(list1)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()