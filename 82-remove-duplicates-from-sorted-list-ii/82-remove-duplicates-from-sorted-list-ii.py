# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0,next=head)
        p, c = temp, head
        while c and c.next:
            if c.val != c.next.val:
                p, c = c, c.next
            else:
                while c.next and c.val == c.next.val:
                    c = c.next
                p.next = c.next
                c = c.next
        
        return temp.next