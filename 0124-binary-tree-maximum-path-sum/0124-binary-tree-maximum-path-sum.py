# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findmaxPath(self,root,maxi):
        if root is None:
            return 0
        leftmax=max(0,self.findmaxPath(root.left,maxi))
        rightmax=max(0,self.findmaxPath(root.right,maxi))
        maxi[0]=max(maxi[0],leftmax+rightmax+root.val)
        return max(leftmax,rightmax)+root.val
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=[float('-inf')] 
        self.findmaxPath(root,maxi)
        return maxi[0]