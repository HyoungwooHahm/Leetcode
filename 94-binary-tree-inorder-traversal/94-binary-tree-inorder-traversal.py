# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output= []
        def Traversal(root):
            temp=root
            if temp:
                Traversal(temp.left)
                output.append(temp.val)
                Traversal(temp.right)
                
        Traversal(root)
        return output
            
        
        