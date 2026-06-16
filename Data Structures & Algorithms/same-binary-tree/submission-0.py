# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #recursively compare left and right subtree

        def sameTree(node1, node2):
            if not node1 and not node2:
                return True #both are empty
            if not node1 or not node2:
                return False #one is empty one is not empty
            if node1.val != node2.val:
                return False #their values are not the same

            #now compare the left and of node 1 and two recursively
            isLeftSame = sameTree(node1.left, node2.left)
            isRightSame = sameTree(node1.right, node2.right)

            return isLeftSame and isRightSame

        return sameTree(p, q)
            
        