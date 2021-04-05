class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr, prev = head, None
        while curr:
            if curr.val == val:
                if not prev:
                    head, curr = curr.next, head
                else:
                    prev.next, curr = curr.next, curr.next
            else:
                prev, curr = curr, curr.next
        return head
