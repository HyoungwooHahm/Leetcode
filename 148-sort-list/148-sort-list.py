# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=head
        s=[]
        
        if l == None:
            return head
        
        while l != None :
            s.append(l.val)
            l=l.next
        
        s.sort()
        
        
        lo=head 
        i=0
        
        while lo != None :
            lo.val=s[i]
            i+=1
            lo=lo.next
        
        return head
        