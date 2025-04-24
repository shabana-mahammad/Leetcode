# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.ValidBST(root,float('-inf'),float('inf'))
    def ValidBST(self,root,minval=float('-inf'),maxval=float('inf')):
        if root==None:
            return True
        if not minval<root.val<maxval:
            return False
        return self.ValidBST(root.left,minval,root.val) and self.ValidBST(root.right,root.val,maxval)