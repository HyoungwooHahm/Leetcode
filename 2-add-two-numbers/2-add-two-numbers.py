# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x=l1
        y=l2
        d=ListNode()
        z=d
        sum=0
        n=0
        
        while x or y :
            if x == None :
                sum = sum + y.val*pow(10,n)
                y=y.next
                
            elif y == None :
                sum  = sum + x.val*pow(10,n)
                x=x.next
            else: 
                sum+=x.val*pow(10,n)+y.val*pow(10,n)
                x=x.next
                y=y.next
            n+=1
        
        temp=sum
        
        for i in range(n+2):
            if int(sum/pow(10,i)) == 0 : 
                continue      
            z.next=ListNode(int(temp%10))
            temp=temp//10
           
            
            z=z.next
            
        if d.next==None :
            return ListNode(0) 
        
        return d.next
            
        