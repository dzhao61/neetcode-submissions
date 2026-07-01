# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inOrder(root, res)
        return res[k-1]


    def inOrder(self, root, lst):
        if not root:
            return
        self.inOrder(root.left, lst)
        lst.append(root.val)
        self.inOrder(root.right, lst)

        