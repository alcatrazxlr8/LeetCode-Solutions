# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2lists(list1, list2):
            tmp = head = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    tmp.next = list1
                    list1 = list1.next
                else:
                    tmp.next = list2
                    list2 = list2.next

                tmp = tmp.next
            
            tmp.next = list1 or list2
            return head.next

        node = tmp = ListNode(-float('inf'))
        for i in range(len(lists)):
            node = merge2lists(lists[i], node)
        
        return node.next




            
