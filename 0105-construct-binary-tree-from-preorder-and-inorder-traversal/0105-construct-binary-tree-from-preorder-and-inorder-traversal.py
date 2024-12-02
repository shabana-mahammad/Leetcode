# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def slove(self,preorder,inorder,start,end,idx):
        if start > end:
            return None,idx
        i=start
        root_val=preorder[idx]
        while i <=end:
            if inorder[i]==root_val:
                break
            i +=1
        idx +=1
        root=TreeNode(root_val)
        root.left, idx = self.slove(preorder,inorder,start,i-1,idx)
        root.right, idx = self.slove(preorder,inorder,i+1,end,idx)
        return root,idx
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx=0
        n=len(preorder)
        root,_= self.slove(preorder,inorder,0,n-1,idx)
        return root