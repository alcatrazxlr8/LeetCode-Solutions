# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ### SET
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return True
            
            visited.add(curr)
            curr = curr.next
            
        return False
            
        
#         ### TORTOISE & HARE [SLOW & FAST POINTER]
#         fast = head
        
#         while fast and fast.next:
#             fast = fast.next.next
#             head = head.next
            
#             if head == fast:
#                 return True
        
#         return False
            