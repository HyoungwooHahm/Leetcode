# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        ans=[]
        queue = [root]
        
        while queue:
            a= queue.pop(0)
            ans.append(a.val)
            if a.left : queue.append(a.left)
            if a.right : queue.append(a.right)
        
        a=1000000000
        
        for i in range(len(ans)):
            for j in range(i+1,len(ans)):
                if abs(ans[i]-ans[j]) < a :
                    a=abs(ans[i]-ans[j])
        
            
        return a
        
        