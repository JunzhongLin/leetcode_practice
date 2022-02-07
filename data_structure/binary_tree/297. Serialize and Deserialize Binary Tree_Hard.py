'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        que = []
        que.append(root)
        serialized = ''
        has_value = True
        while que:
            node = que.pop(0)
            if node != None:
                que.append(node.left)
                que.append(node.right)
            serialized += str(node.val) + ',' if node else 'None,'

        return serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []

        serialized = data.split(',')[:-1]

        root = TreeNode(serialized[0])
        i = 1
        que = [root]
        while que:
            node = que.pop(0)
            if serialized[i] != 'None':
                node.left = TreeNode(serialized[i])
                que.append(node.left)
            i += 1
            if serialized[i] != 'None':
                node.right = TreeNode(serialized[i])
                que.append(node.right)
            i += 1

        return root