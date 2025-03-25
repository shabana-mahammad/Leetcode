# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countgoodNodes(self,root,count,maxi):
        if root is None:
            return None
        if root.val>=maxi:
            count[0] +=1
            maxi=root.val
        self.countgoodNodes(root.left,count,maxi)
        self.countgoodNodes(root.right,count,maxi)

    def goodNodes(self, root: TreeNode) -> int:
        count=[0]
        if not root:
            return count[0]
        self.countgoodNodes(root,count,root.val)
        maxi=root.val
        return count[0] 
