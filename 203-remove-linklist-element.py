class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = ListNode(0)
        prev.next = head
        record = prev
        trav = head
        while trav:
            if trav.val == val:
                prev.next = trav.next
                trav = prev.next
            else:
                prev = trav
                trav = trav.next
        return record.next
