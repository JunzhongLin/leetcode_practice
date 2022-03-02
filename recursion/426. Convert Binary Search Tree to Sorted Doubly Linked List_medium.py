"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        def helper(node):

            if node.left:
                left_most, right = helper(node.left)
                right.right = node
                node.left = right
            else:
                left_most = node

            if node.right:
                left, right_most = helper(node.right)
                node.right = left
                left.left = node
            else:
                right_most = node

            return left_most, right_most

        left, right = helper(root)
        right.right = left
        left.left = right

        return left