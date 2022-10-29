# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:return False
        queue=collections.deque([root])
        s=set()
        while queue:
            n=queue.popleft()
            if n.val not in s and len(s): return False
            s.add(n.val)
            if n.left : queue.append(n.left)
            if n.right : queue.append(n.right)
        
        return True 
            
        