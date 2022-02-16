'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

'''


class TreeNode:
    def __init__(self, val, cnt=1, left=None, right=None):
        self.val = val
        self.cnt = cnt
        self.left = left
        self.right = right


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if nums == []:
            self.root = None

        else:
            self.root = TreeNode(nums[0], )
            for num in nums[1:]:
                self.add(num)

    def add(self, val: int) -> int:

        k = self.k

        if not self.root:
            self.root = TreeNode(val)
        else:
            stack = [self.root]

            while stack:
                node = stack.pop()
                node.cnt += 1

                if node.left and node.val > val:
                    stack.append(node.left)

                elif not node.left and node.val > val:
                    node.left = TreeNode(val)

                elif node.right and node.val <= val:
                    stack.append(node.right)

                elif not node.right and node.val <= val:
                    node.right = TreeNode(val)

        ## search for the k-largest element

        stack = [self.root]

        if self.k > self.root.cnt:
            return

        while stack:
            root = stack.pop()

            if root.right and k > root.right.cnt + 1:
                stack.append(root.left)
                k -= root.right.cnt + 1

            elif root.right and k == root.right.cnt + 1:
                return root.val

            elif not root.right and k > 1:
                stack.append(root.left)
                k -= 1

            elif not root.right and k == 1:
                return root.val

            else:
                stack.append(root.right)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)