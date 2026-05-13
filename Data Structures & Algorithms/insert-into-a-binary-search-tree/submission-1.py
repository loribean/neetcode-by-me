# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     if not root:
    #         return TreeNode(val)

    #     if val > root.val:
    #         root.right = self.insertIntoBST(root.right, val)
    #     elif val < root.val:
    #         root.left = self.insertIntoBST(root.left, val)

    #     return root

# this sollution is slightly more efficient as it saves one call into the call stack
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Handle empty tree case
        if not root:
            return TreeNode(val)

        curr = root

        while True:
            if val > curr.val:
                if not curr.right:
                     # If there's no right child, insert here
                    curr.right = TreeNode(val)
                    break
                # Otherwise, move right
                curr = curr.right
            else:
                if not curr.left:
                    # If there's no left child, insert here
                    curr.left = TreeNode(val)
                    break
                # Otherwise, move left
                curr = curr.left
        return root