'''
Given an n-ary tree, return the level order traversal of its nodes' values.

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
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return None

        q = []
        q.append(root)
        res = []

        while q:
            length = len(q)
            level_res = []
            for _ in range(length):
                node = q.pop(0)
                level_res.append(node.val)
                q.extend(node.children)

            res.append(level_res)

        return res
