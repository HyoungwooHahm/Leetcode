# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        d={}
        def add(root) :
            if root:
                l.append(root.val)
                add(root.left)
                add(root.right)
        add(root)
        for i in set(l):
            if l.count(i) in d:
                d[l.count(i)].append(i)
            else :    
                d[l.count(i)]=[i]
            
        print(d)
            
        return d.get(max(list(d.keys())))
        
        
                
        