# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi=0
    def calculateheight(self,node):
        if not node:
            return 0
        leftheight=self.calculateheight(node.left)
        rightheight=self.calculateheight(node.right)
        self.maxi=max(self.maxi,leftheight+rightheight)
        return 1+max(leftheight,rightheight)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculateheight(root)
        return self.maxi