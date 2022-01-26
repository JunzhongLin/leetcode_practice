'''

Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def postorderTraversal(self, root):
        records =  []

        def traversal(node):
            if not node:
                return
            traversal(node.right)
            records.append(node.val)
            traversal(node.left)

        traversal(root)
        return records

    def postorderTraversal_loop(self, root):
        def postorderTraversal(self, root):
            if not root:
                return []
            stack = [root]
            result = []
            while stack:
                node = stack.pop()
                result.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return result[::-1]

        def postorderTraversal_loop2(self, root):
            result = []
            st = []
            if root:
                st.append(root)
            while st:
                node = st.pop()
                if node != None:
                    st.append(node)  # 中
                    st.append(None)

                    if node.right:  # 右
                        st.append(node.right)
                    if node.left:  # 左
                        st.append(node.left)
                else:
                    node = st.pop()
                    result.append(node.val)
            return result

