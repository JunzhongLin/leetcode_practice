'''
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        stack = []
        stack.append(root)
        res = []

        if not root:
            return None

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.children:
                stack += [n for n in node.children[::-1]]
        return res