# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newHead = ListNode()
        tmp = newHead

        i = list1
        j = list2

        while i and j:
            if i.val <= j.val:
                newHead.next = i
                i = i.next
            else:
                newHead.next = j
                j = j.next
            newHead = newHead.next
        newHead.next = i or j

        return tmp.next