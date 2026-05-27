# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(h) height of the tree | O(h) for recursion stack 
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: if root is None, return None 
        if not root: 
            return None 
        # if key is less, go left 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # if key is greater, go right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found: handle 0 or 1 child cases 
            if not root.left:
                return root.right 
            if not root.right: 
                return root.left 
            # Node with 2 children; get inorder successor 
            min_larger_node = root.right 
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            root.val = min_larger_node.val
            # Delete the inorder successor 
            root.right = self.deleteNode(root.right, min_larger_node.val)

        return root 
