"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copyMap = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            copyMap[curr] = copy
            curr = curr.next
            
        curr = head
        while curr:
            copy = copyMap[curr]
            copy.next = copyMap[curr.next]
            copy.random = copyMap[curr.random]
            curr = curr.next
            
        return  copyMap[head]
        
#         newHead = Node(0, None, None)
#         dummy = newHead
#         oldHead = head
#         while oldHead:
#             tmp = Node(oldHead.val, None, None)
#             dummy.next = tmp
#             dummy = dummy.next
#             oldHead = oldHead.next
        
        
#         while head:
#             print(head.val)
#             head = head.next
        
#         newHead = newHead.next
#         while newHead:
#             print(newHead.val)
#             newHead = newHead.next