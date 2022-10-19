# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        h = {}
        
        def level(r, d):
            if r:
                if d in h:
                    h[d].append(r.val)
                else:
                    h[d] = [r.val]

                level(r.left, d + 1)
                level(r.right, d + 1)
        
        level(root, 0)
        
        ans = []
        for a in h.values():
            ans.append(sum(a)/len(a))
            
        return ans

        