'''

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:

    def maxDepth(self, root: 'Node') -> int:

        self.ans = 0

        def find_maxdepth(root, depth):

            if not root:
                return None

            self.ans = max(self.ans, depth)

            for node in root.children:
                find_maxdepth(node, depth + 1)

        find_maxdepth(root, 1)

        return self.ans