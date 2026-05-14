# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #use DFS to calculate the heights of each node
        #while we calculate left and right, 
        #we can check if tree rooted at current is balanced
        #if left height - right height > 1, updated isBalanced global var

        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]