# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level=[]
        queue=[root]
        while queue:
            l=[]
            for i in range(len(queue)):
                n=queue.pop(0)
                l.append(n.val)
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
            level.append(sum(l))
        print(level)
        return level.index(max(level))+1
            