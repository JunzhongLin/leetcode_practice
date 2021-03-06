'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return

        que = []
        que.append(root)

        while que:

            length = len(que)
            for i in range(length):
                node = que.pop(0)
                if i == length - 1:
                    node.next = None
                else:
                    node.next = que[0]

                if node.left:
                    que.append(node.left)
                    que.append(node.right)

        return root