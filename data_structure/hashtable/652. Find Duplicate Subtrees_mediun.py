'''

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.



'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        node_table = {}
        val_table = {}
        stack = [root]
        res = []
        seen = set()

        while stack:
            node = stack.pop()

            if node == None:
                node = stack.pop()
                val = (
                    node.val,
                    node_table[node.left] if node.left else None,
                    node_table[node.right] if node.right else None
                )

                if val in val_table and val not in seen:
                    res.append(node)
                    seen.add(val)
                node_table[node] = val
                val_table[val] = node
                continue

            stack.append(node)
            stack.append(None)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res