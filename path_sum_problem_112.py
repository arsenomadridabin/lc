# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def sum_vals(root):
            if not root:
                return []
            if not root.left and root.right:
                return [i + root.val for i in sum_vals(root.right)]
            if not root.right and root.left:
                return [i + root.val for i in sum_vals(root.left)]
            if not root.left and not root.right:
                return [root.val]
            else:
                return [i + root.val for i in sum_vals(root.left)] +  [i + root.val for i in sum_vals(root.right)]

        list_of_sum = sum_vals(root)
        if targetSum in list_of_sum:
            return True
        else:
            return False
                
            
        