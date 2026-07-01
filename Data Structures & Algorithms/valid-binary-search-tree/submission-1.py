# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recursiveCheck(root.left, -1001, root.val) and self.recursiveCheck(root.right, root.val, 1001)
        
    def recursiveCheck(self, root, lower, upper):
        if not root:
            return True

        if root.val <= lower or root.val >= upper:
            return False

        return self.recursiveCheck(root.left, lower, root.val) and self.recursiveCheck(root.right, root.val, upper)
