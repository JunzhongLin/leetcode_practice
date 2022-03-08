'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return []

        que = [root]

        left, right = root, root
        while que:
            node = que.pop()
            if node.val > target:
                right = node
                if node.left:
                    que.append(node.left)
            elif node.val < target:
                left = node
                if node.right:
                    que.append(node.right)
            else:
                return node.val

        if abs(left.val - target) < abs(right.val - target):
            return left.val
        else:
            return right.val