# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node=head
        cnt=0
        while node != None:
            node=node.next
            cnt+=1
        
        n=cnt-n
        node=head
        if n==0:
            return head.next
        
        for i in range(n-1):
            node=node.next
            
        node.next=node.next.next
        
        return head
        