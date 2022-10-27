# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        level=[]
        queue=collections.deque([root])
        
        while queue :
            temp=[]
            for i in range(len(queue)):
                n = queue.popleft()
                temp.append(n.val)
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
            level.append(temp)
        
        return sum(level[-1])
            