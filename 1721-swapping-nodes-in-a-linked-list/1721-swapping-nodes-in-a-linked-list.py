# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def arr(Node):
            lst = [] 
            while(Node is not None):
                lst.append(Node.val) 
                Node = Node.next 
            return lst  
        lst = arr(head) 
        lst[k-1], lst[-(k)] = lst[-(k)], lst[k-1] 
        curr = head 
        for i in lst:
            curr.val = i 
            curr = curr.next 
        return head 