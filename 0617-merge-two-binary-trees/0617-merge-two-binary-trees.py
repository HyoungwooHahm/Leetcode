# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None:
            return root2
        if root2 == None:
            return root1
        
        queue1 = collections.deque([root1])
        queue2 = collections.deque([root2])
        
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            if node1 and node2:
                node1.val += node2.val
                
                if not node1.left and node2.left :
                    node1.left = TreeNode(0)
                
                if not node1.right and node2.right:
                    node1.right = TreeNode(0)
            
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)
        
        return root1