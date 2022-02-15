'''

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root]
        prev = None

        while stack:
            node = stack.pop()
            if not node:
                node = stack.pop()
                if prev is not None and node.val <= prev:
                    return False
                prev = node.val
                continue

            if node.right:
                stack.append(node.right)

            stack.append(node)
            stack.append(None)

            if node.left:
                stack.append(node.left)

        return True