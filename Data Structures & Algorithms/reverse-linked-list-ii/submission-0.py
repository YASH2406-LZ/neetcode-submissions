# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        leftPrev = dummy

        # step 1: walk leftPrev to just before position `left`
        for _ in range(left - 1):
            leftPrev = leftPrev.next

        # step 2: reverse the zone
        curr = leftPrev.next      # this is the original `left` node -> becomes tail later
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # step 3: reconnect
        leftPrev.next.next = curr   # old `left` node (now tail) connects to what's after the zone
        leftPrev.next = prev        # node before zone connects to new head of reversed zone

        return dummy.next