# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.check=set([0])
        queue=collections.deque([root])
        root.val=0
        
        if not root : return
        while queue:       
            node=queue.popleft()
            if node.left :
                node.left.val=node.val*2+1
                queue.append(node.left)
                self.check.add(node.left.val)
            if node.right :
                node.right.val=node.val*2+2
                queue.append(node.right)
                self.check.add(node.right.val)

        '''
        def dfs(root, v):
            if root:
                root.val=v
                self.check.add(v)
                dfs(root.left,2*v+1)
                dfs(root.right,2*v+2)
        dfs(root,0)
        '''

            
        

    def find(self, target: int) -> bool:
        return target in self.check
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)