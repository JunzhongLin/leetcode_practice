'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestors_p = set()
        ancestors_q = []
        # search ancestors for node p

        stack = [root]
        while stack:
            node = stack.pop()
            ancestors_p.add(node)
            if node == p:
                break
            if node.val < p.val:
                stack.append(node.right)
            elif node.val > p.val:
                stack.append(node.left)

        # search ancestors for node q

        stack = [root]
        while stack:
            node = stack.pop()
            ancestors_q.append(node)
            if node == q:
                break
            if node.val < q.val:
                stack.append(node.right)
            else:
                stack.append(node.left)

        while ancestors_q:
            node = ancestors_q.pop()
            if node in ancestors_p:
                return node
        return None
