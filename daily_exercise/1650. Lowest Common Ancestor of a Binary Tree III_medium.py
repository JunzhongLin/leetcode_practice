"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_parents, q_parents = [p], [q]

        while p.parent or q.parent:
            if p.parent:
                p_parents.append(p.parent)
                p = p.parent
            if q.parent:
                q_parents.append(q.parent)
                q = q.parent

            if p in q_parents:
                return p
            elif q in p_parents:
                return q