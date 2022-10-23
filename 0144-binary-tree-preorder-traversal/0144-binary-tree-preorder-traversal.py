# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ans=[]
        def preTrav(root):
            if root:
                ans.append(root.val)
                preTrav(root.left)
                preTrav(root.right)
        preTrav(root)
        return ans  """ 
    
        if not root: return []
        ans=[]
        stack = [root]
        while stack:
            a = stack.pop()
            ans.append(a.val)
            if a.right:
                stack.append(a.right)
            if a.left:
                stack.append(a.left)
        return ans
        
        