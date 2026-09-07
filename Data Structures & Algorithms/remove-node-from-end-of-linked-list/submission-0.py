class Solution:
    def removeNthFromEnd(self, head, n):
        
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        head = reverse(head)

        
        if n == 1:
            head = head.next  
        else:
            curr = head
            for _ in range(n - 2):
                curr = curr.next
            curr.next = curr.next.next

        
        head = reverse(head)
        return head