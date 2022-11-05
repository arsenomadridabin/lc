# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.vals = []
        def get_val(root):
            if not root:
                pass
            else:
                self.vals.append(root.val)
                get_val(root.left)
                get_val(root.right)
        get_val(root)
        
        complements = {}
        for i in self.vals:
            if i in complements:
                return True
            else:
                complements[k-i] = True
        return False
        
            
        
        