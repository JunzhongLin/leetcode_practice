'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

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

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder and not preorder:
            return

        que = []
        que.append((inorder, preorder))
        head_node = self._get_node(preorder[0])

        while que:

            length = len(que)
            for _ in range(length):
                inorder, preorder = que.pop(0)
                root = self._get_node(preorder[0])

                if len(inorder) == 1:
                    continue

                for i, node in enumerate(inorder):
                    if node == root.val:
                        break
                left_inorder = inorder[:i]
                right_inorder = inorder[i + 1:]

                left_preorder = preorder[1:len(left_inorder) + 1]
                right_preorder = preorder[len(left_inorder) + 1:]

                if left_inorder:
                    que.append((left_inorder, left_preorder))
                    root.left = self._get_node(left_preorder[0])

                if right_inorder:
                    que.append((right_inorder, right_preorder))
                    root.right = self._get_node(right_preorder[0])

        return head_node