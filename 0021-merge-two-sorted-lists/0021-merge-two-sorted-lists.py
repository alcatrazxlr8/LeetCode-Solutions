# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        newNode = tmpNode = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tmpNode.next = list1
                # tmpNode = tmpNode.next
                list1 = list1.next
            else:
                tmpNode.next = list2
                # tmpNode = tmpNode.next
                list2 = list2.next
            tmpNode = tmpNode.next

        tmpNode.next = list1 or list2
        
        return newNode.next
            
