# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(log n) for Balanced Tree
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Traverse the BST recursively 
        # If current node is None, insert here
        if not root:
            return TreeNode(val)
        # Go left if al is less than current node 
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        #. Go right if val is greater than current node 
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root 
        
        