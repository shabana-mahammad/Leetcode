# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, postorder, inorder,start,end,idx):
        if start > end:
            return None, idx
        root_val=postorder[idx]
        i=start
        while i <=end:
            if inorder[i]==root_val:
                break
            i +=1
        idx -=1
        root=TreeNode(root_val)
        root.right,idx =self.solve(postorder, inorder,i+1,end,idx)
        root.left,idx =self.solve(postorder, inorder, start,i-1,idx)
        return root,idx

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n=len(postorder)
        idx=n-1
        root, _ = self.solve(postorder, inorder, 0,n-1,idx)
        return root