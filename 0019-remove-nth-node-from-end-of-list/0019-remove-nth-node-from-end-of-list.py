# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        cnt = 0
        while tmp:
            tmp = tmp.next
            cnt += 1
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        if cnt == n:
            head = head.next
            return head
        
        for i in range(cnt-n):
            prev = prev.next
            curr = curr.next
        
        prev.next = curr.next
        
        return head
