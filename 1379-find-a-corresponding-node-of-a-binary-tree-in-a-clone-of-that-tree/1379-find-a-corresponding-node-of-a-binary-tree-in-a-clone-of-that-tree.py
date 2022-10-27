# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original : return None
        
        queue=collections.deque([cloned])
        
        while queue:
            n = queue.popleft()
            if n.val == target.val : return n
            if n.left : 
                queue.append(n.left)
            if n.right:
                queue.append(n.right)        