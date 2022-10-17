# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
                
        def Symmetric(left, right):
            if not left and not right: 
                return True
            if not left or not right:
                return False
            
            return left.val == right.val and Symmetric(left.left, right.right) and Symmetric(left.right, right.left)
        
        return Symmetric(root.left, root.right)
        