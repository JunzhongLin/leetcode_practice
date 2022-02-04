'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        node_stack = []
        node_stack.append((root, targetSum - root.val))

        while node_stack:
            node, curr_sum = node_stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                node_stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                node_stack.append((node.left, curr_sum - node.left.val))

        return False

    def hasPathSum_recur(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum = targetSum - root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum_recur(root.left, targetSum) or self.hasPathSum_recur(root.right, targetSum)
