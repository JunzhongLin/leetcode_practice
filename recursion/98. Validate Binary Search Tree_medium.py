'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        if root.left:
            isvalid_left = self.isValidBST(root.left)
        else:
            isvalid_left = None
        if root.right:
            isvalid_right = self.isValidBST(root.right)
        else:
            isvalid_right = None

        condition1 = (isvalid_left and isvalid_right and self.search_max(root.left) < root.val < self.search_min(
            root.right))
        condition2 = (isvalid_left and isvalid_right is None and self.search_max(root.left) < root.val)
        condition3 = (isvalid_right and isvalid_left is None and self.search_min(root.right) > root.val)
        if condition1 or condition2 or condition3:
            return True

        return False

    def search_max(self, node):
        if not node.right:
            return node.val
        node = node.right
        return self.search_max(node)

    def search_min(self, node):
        if not node.left:
            return node.val
        node = node.left
        return self.search_min(node)