# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root== None:
            return True
        return self.isSymmerticsHelp(root.left,root.right)

    def isSymmerticsHelp(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val!=right.val:
            return False
        return (self.isSymmerticsHelp(left.left, right.right) and self.isSymmerticsHelp(left.right, right.left))