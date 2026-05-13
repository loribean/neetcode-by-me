# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #to delete a node, we first need to find it
    #once we find it, we need to know if it is either
    #case 1 : 0 - 1 children
    #case 2: 2 children
    #for case 1, simple; just return the right or left node or null
    #for case 2, we need to find the min node of right tree (its confirm a leaf), then
    #then we need make the root.val the min value
    #then delete the min value from the root right sub tree
    def findMinNode(self, root: Optional[TreeNode]):
        current = root
        while current and current.left:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        #base case if root dont even exist
        if not root:
            return None
        
        #lets start searching
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #we found the node!
            #we handle case 1
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                #there is both right and left child
                minNode = self.findMinNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

        return root
                


        