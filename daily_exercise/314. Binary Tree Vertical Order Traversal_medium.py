# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        temp_res, res = defaultdict(list), []

        que = [(root, 0)]
        while que:
            for _ in range(len(que)):
                node, i = que.pop(0)
                if not node:
                    return res
                if node:
                    temp_res[i].append(node.val)
                if node.left:
                    que.append((node.left, i - 1))
                if node.right:
                    que.append((node.right, i + 1))

        for i in range(min(temp_res.keys()), max(temp_res.keys()) + 1):
            if i in temp_res:
                res.append(temp_res[i])

        return res