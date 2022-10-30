# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [(root,None,0)]
        
        while queue:
            
            cur, parent, level = queue.pop(0)
            
            if cur.val == x:
                x_parent = parent
                x_level = level
            
            if cur.val == y:
                y_parent = parent
                y_level = level
            
            if cur.left:
                queue.append((cur.left,cur,level+1))
            if cur.right:
                queue.append((cur.right,cur,level+1))
        
        return x_parent != y_parent and x_level == y_level