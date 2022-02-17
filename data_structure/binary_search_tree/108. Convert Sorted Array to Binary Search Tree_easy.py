'''

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None

        m = len(nums)
        queue_nums = [nums[:m // 2], nums[m // 2 + 1:]]
        root = TreeNode(nums[m // 2])
        queue_nodes = [root]

        while queue_nodes:
            node = queue_nodes.pop(0)

            left_nums = queue_nums.pop(0)
            m_left = len(left_nums)
            if left_nums:
                node.left = TreeNode(left_nums[m_left // 2])
                queue_nums.extend([left_nums[:m_left // 2], left_nums[m_left // 2 + 1:]])
                queue_nodes.append(node.left)

            right_nums = queue_nums.pop(0)
            m_right = len(right_nums)
            if right_nums:
                node.right = TreeNode(right_nums[m_right // 2])
                queue_nums.extend([right_nums[:m_right // 2], right_nums[m_right // 2 + 1:]])
                queue_nodes.append(node.right)

        return root
