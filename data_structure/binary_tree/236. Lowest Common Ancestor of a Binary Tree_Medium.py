'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

'''


class Solution:
    def lowestCommonAncestor_TLE(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor_set_p = set()
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if not node:
                stack.pop()
                continue

            if node == 'found p':
                ancestor_set_p.add(stack.pop())
                while stack:
                    node = stack.pop()
                    if not node:
                        ancestor_set_p.add(stack.pop())
                    else:
                        continue
                break

            stack.append(node)
            if node == p:
                stack.append('found p')
                continue
            stack.append(None)

            if node.right:
                stack.append(node.right)
                if node.right == p:
                    stack.append('found p')
                    continue

            if node.left:
                stack.append(node.left)
                if node.left == p:
                    stack.append('found p')
                    continue

        stack_q = []
        stack_q.append(root)

        while stack_q:
            node = stack_q.pop()

            if not node:
                stack_q.pop()
                continue

            if node == 'found q':
                ancestor_q = stack_q.pop()
                if ancestor_q in ancestor_set_p:
                    return ancestor_q
                while stack_q:
                    node = stack_q.pop()
                    if not node:
                        ancestor_q = stack_q.pop()
                        if ancestor_q in ancestor_set_p:
                            return ancestor_q
                    else:
                        continue
                break

            stack_q.append(node)
            if node == q:
                stack_q.append('found q')
                continue
            stack_q.append(None)

            if node.right:
                stack_q.append(node.right)
                if node.right == q:
                    stack_q.append('found q')
                    continue

            if node.left:
                stack_q.append(node.left)
                if node.left == q:
                    stack_q.append('found q')
                    continue

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
