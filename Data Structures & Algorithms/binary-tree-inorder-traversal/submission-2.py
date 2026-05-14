# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #imitate recursive call stack using an explicit stack. 

        stack = []
        curr = root
        res = []

        while curr or stack:
            while curr:
                #While the current node is not null, push it onto the stack and move to its left child.
                stack.append(curr)
                curr = curr.left
            #Pop a node from the stack, add its value to the result.
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
           # Move to the right child of the popped node. Then maybe explore its left node

        return res