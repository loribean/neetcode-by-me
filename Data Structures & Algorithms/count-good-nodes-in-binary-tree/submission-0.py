# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs
        #start with root, root is always good node
        #traverse down each path, and with it, take the maximum we have encountered so far
        #for the first iteration, we will compare with the root node.
        #if the node < max, its not a good node
        #if node > max, its a good node & also the newest max
        #repeat with the right side

        goodNodes = []

        def dfs(node,maxThusFar):
            if not node:
                return 
            if node.val >= maxThusFar:
                goodNodes.append(node)
                maxThusFar = node.val
            dfs(node.left, maxThusFar)
            dfs(node.right, maxThusFar)

        dfs(root, root.val)
        
        return len(goodNodes)

