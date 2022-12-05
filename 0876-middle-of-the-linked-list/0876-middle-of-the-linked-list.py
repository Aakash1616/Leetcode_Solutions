# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        while(head.next and head.next.next):
            curr = curr.next 
            head = head.next.next 
        if head.next:
            return curr.next 
        return curr 