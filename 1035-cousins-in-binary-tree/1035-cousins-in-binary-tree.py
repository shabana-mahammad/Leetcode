# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,parent,value,height):
        if not root:
            return []
        if root.val==value:
            return height
        parent[0]=root.val
        left=self.solve(root.left,parent,value,height+1)
        if left:
            return left
        parent[0]=root.val
        right=self.solve(root.right,parent,value,height+1)
        if right:
            return right
        
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        if root.val==x or root.val==y:
            return False
        xParent=[-1]
        xHeight=self.solve(root,xParent,x,0)
        yParent=[-1]
        yHeight=self.solve(root,yParent,y,0)
        if xParent[0]!=yParent [0] and xHeight==yHeight:
            return True
        return False