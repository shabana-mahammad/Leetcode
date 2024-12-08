# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def dfs(self,root,mp,res):
        if not root:
            return "NULL"
        subtree= f"{root.val},{self.dfs(root.left,mp,res)},{self.dfs(root.right,mp,res)}"
        if mp[subtree]==1:
            res.append(root)
        mp[subtree] +=1
        return subtree
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mp=defaultdict(int)
        res=[]
        self.dfs(root,mp,res)
        return res
        