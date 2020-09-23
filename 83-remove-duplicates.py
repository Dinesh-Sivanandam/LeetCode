
#program for removing the duplicates in the linked list

class Solution(object):
    
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #if the head value is None we are returning simply head
        if head == None:
            return head
        #else we are assaigning current value as head.next and prev as head
        current = head.next
        prev = head

        """
        while the current value not equal to null
        and if current value equal to prev number
        we are changing prev.next = current.next to dereference the current value
        and current = current.next

        else
        we are just going to next value of current and prev
        """
        while current != None:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next

        #returning the head
        return head



