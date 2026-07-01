# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.globMax = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recursiveMax(root)
        return self.globMax
    
    def recursiveMax(self, node):
        if not node:
            return 0
        lDepth = self.recursiveMax(node.left)
        rDepth = self.recursiveMax(node.right)
        curr = lDepth + rDepth
        self.globMax = max(curr, self.globMax)
        return max(lDepth, rDepth) + 1

