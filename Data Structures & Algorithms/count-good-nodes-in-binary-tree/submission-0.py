# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.recursiveGood(root, root.val)

    
    def recursiveGood(self, node, x):
        if node is None:
            return 0
        
        if node.val >= x:
            return 1 + self.recursiveGood(node.left, node.val) + self.recursiveGood(node.right, node.val)
        
        if node.val < x:
            return self.recursiveGood(node.left, x) + self.recursiveGood(node.right, x)
        