# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nodeLst = [root]
        res = [[root.val]]

        while nodeLst:
            temp = []
            vals = []
            for node in nodeLst:
                if node.left:
                    temp.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    vals.append(node.right.val)
            if vals:
                res.append(vals)
            nodeLst = temp
            
        return res

        