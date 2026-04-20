# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes=[]
        for i in lists:
            while i:
                nodes.append(i.val)
                i=i.next
        nodes.sort()
        res=ListNode(0)
        r=res
        for i in nodes:
            res.next=ListNode(i)
            res=res.next
        return r.next