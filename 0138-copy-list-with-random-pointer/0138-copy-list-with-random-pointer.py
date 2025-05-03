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
        
        # copyMap = {None: None} ## need this for copyMap[curr.next] and copyMap[curr.random] since they could be NULL / None
        copyMap = {}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            copyMap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = copyMap[curr]
            # copy.next = copyMap[curr.next]
            copy.next = copyMap.get(curr.next)
            # copy.random = copyMap[curr.random]
            copy.random = copyMap.get(curr.random)
            curr = curr.next

        return copyMap.get(head)