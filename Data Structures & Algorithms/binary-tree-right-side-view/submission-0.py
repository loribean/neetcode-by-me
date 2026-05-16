# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #lets do bfs
        #collect each level
        #return the last of each level

        queue = deque([root])
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
                res.append(level_res[-1])
        return res


        
        