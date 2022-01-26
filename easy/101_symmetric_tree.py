'''

Given the root of a binary tree,
check whether it is a mirror of itself (i.e., symmetric around its center).

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left  = n2
n1.right = n3

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(root1, root2):
            if root1 == root2 == None: return True
            if not root1 or not root2: return False
            if root1.val != root2.val: return False
            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        if not root: return True
        return dfs(root.left, root.right)