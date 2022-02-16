'''

Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        prev = None
        while stack:
            node = stack.pop()
            if not node:
                node = stack.pop()
                if prev == p:
                    return node
                prev = node
                continue

            if node.right:
                stack.append(node.right)

            stack.append(node)
            stack.append(None)

            if node.left:
                stack.append(node.left)

        return None