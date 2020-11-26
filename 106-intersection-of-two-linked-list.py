
#Creating the class node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
#Creating the class for linked list
class LinkedList:
    #this statement initializes when created
    #initializing head is none at initial
    def __init__(self):
        self.head = None
    
    """
    function to insert the set of values in the linked list
    this function gets the list of values
    then iterate through the list values one by one
    then insering the value to the end by insert_at_end function
    """
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    #there given the skip value in the code
    #we can use the skip value to get the intersection point
    #else we use below function to get the intersection value
    def skip(self, l1, skip1):

        i = 1
        
        itr = self.head
        
        while itr:
            if i > skip1:
                return itr.data
            itr = itr.next
            i += 1

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #placing the values of the head
        curA,curB = headA,headB
        
        #initializing the length of two linked list as 0
        lenA,lenB = 0,0
        
        #getting the length by using loop
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
            
        #again placing the head values for iteration
        curA,curB = headA,headB
        
        """
            if the length of a is greater then b incrementing the cura value
            else if the len of b is greater incrementing the curb value
        """
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
                
        #while value of curb not equal to value of cura
        #incrementing curb value and cura value
        #if we came with the false statement we are in the intersection point
        while curB != curA:
            curB = curB.next
            curA = curA.next
            
        #then returning the intersection point
        return curA
        
if __name__ == '__main__':
    ll = LinkedList()
    l2 = LinkedList()
    ll.insert_values([4,1,8,4,5])
    l2.insert_values([5,6,1,8,4,5])
    skip1 = 2
    skip2 = 3
    result = ll.skip(ll, skip1)
    print("The intresection point is %d" %result)
