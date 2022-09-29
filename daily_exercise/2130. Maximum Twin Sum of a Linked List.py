
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:

        ans, list_size, node = 0, 0, head
        val_list = []

        while node:
            val_list.append(node.val)
            list_size += 1
            node = node.next

        for i in range(int(list_size / 2)):
            ans = max(val_list[i] + val_list[list_size - i - 1], ans)

        return ans


#'ef pairSum(self, head: Optional[ListNode]) -> int:
#	slow, fast = head, head
#	maxVal = 0

#	# Get middle of linked list
#	while fast and fast.next:
#		fast = fast.next.next
#		slow = slow.next

#	# Reverse second part of linked list
#	curr, prev = slow, None

#	while curr:
#		curr.next, prev, curr = prev, curr, curr.next

#	# Get max sum of pairs
#	while prev:
#		maxVal = max(maxVal, head.val + prev.val)
#		prev = prev.next
#		head = head.next

#	return maxVal
