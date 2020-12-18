# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        pre = None
        cur = head
        '''
        Taking the value one by one and moving it forward tomake it reverse
        '''
        while cur:
            # record pointer to the next node 
            # cuz we'll change the pointer of cur node to pre node,
            # but we still want to move forward
            nextTemp = cur.next
            # reverse the pointer of current node to the pre one
            cur.next = pre
            # update pre & cur pointer
            pre = cur
            cur = nextTemp
        
        return pre