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

        # DFS function returns isBalanced bool & height
        def dfs(root):
            if not root:
                return [True, 0]
            #recursively get results from left & right children
            left, right = dfs(root.left), dfs(root.right)
            #its balanced if left and right subtrees are balanced
            #and if this node is balanced
            #which means, its left and right are balanced
            #which means, the absolute diff between left and right is not more than 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            #return the value of balanced + the heght of the current node (1+ max height of children)
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]