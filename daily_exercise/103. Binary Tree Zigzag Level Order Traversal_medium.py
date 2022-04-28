# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        que = [root]
        res = []
        reverse = 1
        while que:
            reverse *= -1
            level_res = []
            for _ in range(len(que)):
                node = que.pop(0)
                level_res.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if reverse == 1:
                level_res.reverse()

            res.append(level_res)
        return res