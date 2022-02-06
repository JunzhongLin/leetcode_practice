'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def __init__(self, ):
        self.node_set = {}

    def _get_node(self, node_val):

        if node_val in self.node_set:
            return self.node_set[node_val]
        else:
            self.node_set[node_val] = TreeNode(val=node_val)
            return self.node_set[node_val]

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder and not postorder:
            return

        que = []
        que.append((inorder, postorder))
        head_node = self._get_node(postorder[-1])

        while que:

            length = len(que)
            for _ in range(length):
                inorder, postorder = que.pop(0)
                root = self._get_node(postorder[-1])

                if len(inorder) == 1:
                    continue

                for i, node in enumerate(inorder):
                    if node == root.val:
                        break
                left_inorder = inorder[:i]
                right_inorder = inorder[i + 1:]

                left_postorder = postorder[:len(left_inorder)]
                right_postorder = postorder[len(left_inorder):-1]

                if left_inorder:
                    que.append((left_inorder, left_postorder))
                    root.left = self._get_node(left_postorder[-1])

                if right_inorder:
                    que.append((right_inorder, right_postorder))
                    root.right = self._get_node(right_postorder[-1])

        return head_node