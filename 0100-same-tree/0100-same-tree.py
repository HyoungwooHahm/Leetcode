# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        def preOrder(t1,t2):
            if t1 == None and t2 == None : return True
            if t1 == None or t2 == None or t1.val != t2.val : return False    
            return preOrder(t1.left, t2.left) and preOrder(t1.right, t2.right)

        return preOrder(p,q)
        '''
        if not p and not q : return True
        if not p or not q : return False
   

        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            a = stack1.pop()
            b = stack2.pop()
            
            if a.val != b.val : return False
            if a.right == None and b.right : return False
            if b.right == None and a.right : return False
            if a.left == None and b.left : return False
            if b.left == None and a.left : return False
            
            if a.right:
                stack1.append(a.right)
            if a.left:
                stack1.append(a.left)
            if b.right:
                stack2.append(b.right)
            if a.left:
                stack2.append(b.left)
                
        return True

        

                
                
                
   
