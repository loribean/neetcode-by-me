# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we use dfs to traverse the the nodes inorder
        # we use a counter variable to keep track of the position of current node
        # once we hit k, we can return
        counter = k
        res = root.val
        def inorder(node):
            nonlocal counter, res
            if not node:
                return
            inorder(node.left)
            if counter == 0:
                return
            counter -= 1
            if counter == 0:
                res = node.val
                return
            inorder(node.right)

        inorder(root)
        return res
            

        