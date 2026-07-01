# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.recursiveInvert(root)
        return root
    
    
    def recursiveInvert(self, node):
        if node.left or node.right:
            temp = node.right
            node.right = node.left
            node.left = temp
        if node.left:
            self.recursiveInvert(node.left)
        if node.right:
            self.recursiveInvert(node.right)
