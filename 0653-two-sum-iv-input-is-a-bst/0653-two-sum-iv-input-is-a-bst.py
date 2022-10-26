# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root : return False
        l=[]
        queue=[root]
        while queue:
            n=queue.pop(0)
            r=k-n.val
            if n.val in l : return True
            l.append(r)
            if n.left: queue.append(n.left)
            if n.right: queue.append(n.right)
        
        return False
       