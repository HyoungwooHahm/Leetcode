"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':       
        
        if not root: return root

        queue = [root]
   
        
        while queue:
            l=len(queue)

            for i in range(l):
                a = queue.pop(0)
                if i+1 < l:
                    a.next=queue[0]
                if a.left:  
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
    
        return root
    
