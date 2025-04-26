# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,k):
        if root is None:
            return 0
        left=self.solve(root.left,k)
        if left:
            return left 
        k[0] -=1 
        if k[0]==0:
            return root.val
        right=self.solve(root.right,k)
        return right
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.solve(root,[k])