# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #inverting a tree means swapping its left and right children

        if not root:
            return root


        def invert(node):
            node.right, node.left = node.left, node.right
            
            if node.right:
                invert(node.right)
            if node.left:
                invert(node.left)

        invert(root)

        return root
