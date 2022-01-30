'''
Given the root of a binary tree, return the inorder traversal of its nodes' values

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def inorderTraversal(self, root):
        records = []

        def traversal(node):
            if not node:
                return
            traversal(node.left)
            records.append(node.value)
            traversal(node.right)

        traversal(root)
        return records

    def inorderTraversal_loop(self, root):

        records = []
        node_stack = []
        cur = root

        while cur or node_stack:

            if cur:
                node_stack.append(cur)
                cur =cur.left
            else:
                cur = node_stack.pop()
                records.append(cur.val)
                cur=cur.right
        return records

    def inorderTraversal_loop_2(self, root):
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right:  # 添加右节点（空节点不入栈）
                    st.append(node.right)

                st.append(node)  # 添加中节点
                st.append(None)  # 中节点访问过，但是还没有处理，加入空节点做为标记。

                if node.left:  # 添加左节点（空节点不入栈）
                    st.append(node.left)
            else:  # 只有遇到空节点的时候，才将下一个节点放进结果集
                node = st.pop()  # 重新取出栈中元素
                result.append(node.val)  # 加入到结果集
        return result
