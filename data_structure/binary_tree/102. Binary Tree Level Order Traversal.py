'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to
right, level by level)

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        results = []
        if not root:
            return results

        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)

        return results


class Solution_n:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        que = []
        que.append(root)

        res = []

        if root is None:
            return []

        while que:
            level_res = []
            level_length = len(que)
            for i in range(level_length):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                level_res.append(node.val)

            res.append(level_res)

        return res