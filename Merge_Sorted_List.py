# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        input:
        l1=[1,2,4]
        l2=[1,3,4]
        Output: [1,1,2,3,4,4]
        Approach: Linked List with Recursion
        """
        if l1 and l2: #if l1 and l2 are not null
            if l1.val>l2.val: #if n1 node value is bigger than l2 node.
                l1,l2=l2,l1 #swap for sorting
            l1.next = self.mergeTwoLists(l1.next,l2) #recursion function
        return l1 or l2 #if either l1 or l2 has no more node to traverse, it will return the sorted merge linked lists
