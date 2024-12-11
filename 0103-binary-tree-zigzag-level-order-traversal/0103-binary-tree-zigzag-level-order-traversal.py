# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        queue=deque([root])
        if not root:
            return ans
        leftToright=True
        while queue:
            size=len(queue)
            level=[0]*size
            for i in range(size):
                node=queue.popleft()
                index=i if leftToright else(size-1-i)
                level[index]=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            leftToright = not leftToright
            ans.append(level)
        return ans
