# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        of = 0
        dummy = ListNode(0)
        tmp = dummy
        while(l1 or l2):
            if l1:
                x = l1.val
            else:
                x = 0
                
            if l2:
                y = l2.val
            else:
                y = 0
                
            sum = x + y + of
            of = sum//10
            sum = sum%10
            tmp.next = ListNode(sum)
            tmp = tmp.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if of:
            node = ListNode(of)
            tmp.next = node
                
        return dummy.next 
    
    