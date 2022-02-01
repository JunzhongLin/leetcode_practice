'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        add = 0
        dummy = ListNode(next=l1)
        prev = dummy

        while (l1 or l2) or add > 0:

            if l1 and l2:

                l1.val, add = (add + l1.val + l2.val) % 10, (add + l1.val + l2.val) // 10

                prev = prev.next
                l1, l2 = l1.next, l2.next

            elif l1 and (l2 is None):

                l1.val, add = (add + l1.val) % 10, (add + l1.val) // 10
                l1 = l1.next
                prev = prev.next

            elif (l1 is None) and l2:

                prev.next = l2
                l2.val, add = (add + l2.val) % 10, (add + l2.val) // 10
                l2 = l2.next
                prev = prev.next

            elif l2 is None and l1 is None and add > 0:
                prev.next = ListNode(add)
                add = 0

        return dummy.next
