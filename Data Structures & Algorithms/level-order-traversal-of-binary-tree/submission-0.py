# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #use bfs to traverse
        queue = deque([root])
        level = 0
        res = []

        while len(queue) > 0:

            level_res = []
            for i in range(len(queue)):
                current = queue.popleft()
                if current:
                    level_res.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
            if level_res:
                res.append(level_res)

        return res