# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slowHead = head
        fastHead = head
        while(fastHead and fastHead.next):
            slowHead = slowHead.next
            fastHead = fastHead.next.next
            if slowHead == fastHead:
                return True
        return False