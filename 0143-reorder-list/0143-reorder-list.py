# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return

        # find center
        def findCenter(head) -> ListNode:
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            center = slow.next
            slow.next = None
            return center

        # reverse 2nd half - from center to end
        def reverse(head):
            center = findCenter(head)
            prev = None
            curr = center
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tail = prev
            return tail

        start, tail = head, reverse(head)

        while tail:
            startNext = start.next
            tailNext = tail.next
            start.next = tail
            tail.next = startNext
            start = startNext
            tail = tailNext


