# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if not root:
            return []
        ans, queue = [], [(root, "")]
        while queue:
            node, l = queue.pop(0)
            if not node.left and not node.right:
                ans.append(l+str(node.val))
            if node.left:
                queue.append((node.left, l+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, l+str(node.val)+"->"))
        return ans