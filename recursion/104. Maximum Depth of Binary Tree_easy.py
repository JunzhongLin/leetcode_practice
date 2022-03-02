'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth_iter(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        ans = 0
        que = []
        que.append(root)

        while que:
            ans += 1

            length = len(que)
            for i in range(length):
                root = que.pop(0)
                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)

        return ans

    def __init__(self):
        self.ans = 0

    def maxDepth_bu(self, root):
        depth = 1

        def find_maxdepth(root, depth):
            if root is None:
                return

            self.ans = max(self.ans, depth)

            find_maxdepth(root.left, depth + 1)
            find_maxdepth(root.right, depth + 1)

        find_maxdepth(root, depth)

        return self.ans

    def maxDepth(self, root):

        def helper(node):
            if not node:
                return 0
            depth = max(helper(node.left), helper(node.right)) + 1
            return depth

        return helper(root)