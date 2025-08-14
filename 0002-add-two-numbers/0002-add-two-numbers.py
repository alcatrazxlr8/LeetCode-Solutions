# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        ans = ListNode()
        res = ans
        of = 0
        while l1 or l2 or of:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            add = of + num1 + num2
            num = (add) % 10
            of = (add) // 10
            ans.next = ListNode(num)
            ans = ans.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return res.next