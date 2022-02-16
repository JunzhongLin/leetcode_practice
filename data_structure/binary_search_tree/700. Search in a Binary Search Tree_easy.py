'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == val:
                return node

            if node.val < val and node.right:
                stack.append(node.right)
                continue

            if node.val > val and node.left:
                stack.append(node.left)
                continue

            if not node.left and not node.right:
                return None
