'''
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None

        stack = []
        stack.append(root)
        res = []

        while stack:
            node = stack.pop()

            if node is None:
                res.append(stack.pop().val)

            else:

                stack.append(node)
                stack.append(None)

                if node.children:
                    stack.extend(node.children[::-1])
        return res