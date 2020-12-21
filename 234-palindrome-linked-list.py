# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    
    
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next
        
        if len(node_list) == 0:
            return True
        if len(node_list) == 1:
            return True
        elif node_list == node_list[::-1]:
            return True
        return False
