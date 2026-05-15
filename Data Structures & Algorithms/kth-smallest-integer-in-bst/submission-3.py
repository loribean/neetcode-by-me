# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use dfs to traverse the tree in order
        # use a stack to stimulate callstack
        # once k has been depleted, we found our value

        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left #basically checking if left child exists
            #curr doesnt exist anymore, meaning the theres no left child
            #lets get the item that was last pushed
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right # curr is now repopulated so we go back to check if it has left children
            #if it doesnt, we examine it as it is and pop out values till we deplete k

        