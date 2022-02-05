# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, ptr1, ptr2):
        head = ListNode(0)
        curr = head
        while(ptr1 and ptr2):
            if ptr1.val<ptr2.val:
                curr.next = ptr1
                ptr1 = ptr1.next
            else:
                curr.next = ptr2
                ptr2 = ptr2.next
            curr = curr.next
        if ptr1:
            curr.next = ptr1 
        if ptr2:
            curr.next = ptr2
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        ind = 1 
        while(ind < l):
            for i in range(0, l - ind, ind*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+ind])
            ind*=2 
        return lists[0] if l > 0 else None