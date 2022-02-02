'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

'''
# this is a test for branching

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# edited from master branch

class Solution:

    def preorderTraversal(self, root):

        records= []

        def traversal(root):
            if not root:
                return
            records.append(root.val)
            traversal(root.left)
            traversal(root.rigth)

        traversal(root)

        return records

    def preorderTraversal_loop(self, root):
        if not root:
            return []

        records = []
        node_stack = [root]
        while node_stack:
            node = node_stack.pop()
            records.append(root.val)
            if node.right:
                node_stack.append(root.right)
            if node.left:
                node_stack.append(root.left)

        return records

    def preorderTraversal_2(self, root):
        result = []
        st= []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right: #右
                    st.append(node.right)
                if node.left: #左
                    st.append(node.left)
                st.append(node) #中
                st.append(None)
            else:
                node = st.pop()
                result.append(node.val)
        return result