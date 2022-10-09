# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr=[]
        check=True
        def inOrder(root):

            temp=root
            if temp:
                inOrder(temp.left)
                arr.append(temp.val)
                inOrder(temp.right)
         

        inOrder(root)
        for i in range(len(arr)-1):
            if arr[i]>= arr[i+1]:
                check=False
                break
        return check
                
            
        