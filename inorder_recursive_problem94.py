# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        data = []
        def inorder(root):
            if not root:
                pass
            else:
                inorder(root.left)
                data.append(root.val)
                inorder(root.right)
        inorder(root)
        
        return data