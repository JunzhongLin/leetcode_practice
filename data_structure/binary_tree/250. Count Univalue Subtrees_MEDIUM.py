''''
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self, ):
        self.count = 0

    def countUnivalSubtrees_recur(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def count_subtrees(root, ):
            if not root:
                return None

            if not root.left and not root.right:
                self.count += 1
                return root.val

            left_val = count_subtrees(root.left)
            right_val = count_subtrees(root.right)

            if left_val and right_val:
                if left_val == right_val == root.val:
                    self.count += 1
                    return root.val
                return False

            else:
                if left_val is False or right_val is False:
                    return False
                if (left_val or right_val) == root.val:
                    self.count += 1
                    return root.val
                return False

        count_subtrees(root)

        return self.count

    def countUnivalSubtrees_iter(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = []
        stack.append((root, root.left, root.right))

        while stack:

            root, _, _ = stack.pop()

            if root != None:
                stack.append((root, root.left, root.right))
                stack.append((None, None, None))

                if root.left:
                    stack.append((root.left, root.left.left, root.left.right))
                if root.right:
                    stack.append((root.right, root.right.left, root.right.right))
            else:
                root, left, right = stack.pop()
                if not left and not right:
                    self.count += 1
                elif left and right:
                    if str(left.val) == 'False' or str(right.val) == 'False':
                        root.val = False
                    elif root.val == left.val == right.val:
                        self.count += 1
                    else:
                        root.val = False
                else:
                    if (right or left).val is False:
                        root.val = False
                    elif (left or right).val == root.val:
                        self.count += 1
                    else:
                        root.val = False

        return self.count