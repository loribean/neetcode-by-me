# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #same as same tree
        #check both left and right subtrees
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root,subRoot):
            return True #the root is the same and the given tree
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))
    
        
    def sameTree(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        
        isLeftSame = self.sameTree(node1.left, node2.left)
        isRightSame = self.sameTree(node1.right, node2.right)

        return isLeftSame and isRightSame
        
        
        


        