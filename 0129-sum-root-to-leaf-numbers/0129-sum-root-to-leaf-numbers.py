# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,val):
        if not root:
            return []
        val = val * 10 + root.val
        if not root.left and not root.right:
            self.ans +=val
            return 
        self.dfs(root.left,val)
        self.dfs(root.right,val)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans=0
        self.dfs(root,0)
        return self.ans