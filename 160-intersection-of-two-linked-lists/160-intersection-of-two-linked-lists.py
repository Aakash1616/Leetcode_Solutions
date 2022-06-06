# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None: return 
        
        ptra, ptrb = headA, headB 
        
        while(ptra!=ptrb):
            ptra = headB if ptra is None else ptra.next 
            ptrb = headA if ptrb is None else ptrb.next  
            
        return ptra 