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
        queue = collections.deque()
        res = []
        queue.append(root)

        while queue:
            qLen = len(queue)
            level_res = []

            for i in range(qLen):
                current = queue.popleft()

                if current:
                    level_res.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)

            if level_res:
                res.append(level_res)

        return res