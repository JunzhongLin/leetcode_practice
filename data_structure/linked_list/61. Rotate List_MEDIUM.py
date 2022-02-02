'''
Given the head of a linked list, rotate the list to the right by k places.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1, next=head)
        dummy_tail = ListNode(-2, next=None)

        self._count = 0

        slow, fast = head, head

        if not head or not head.next or k == 0:
            return head

        while fast.next:
            fast = fast.next
            self._count += 1

        dummy_tail.next = fast
        fast.next = dummy_head.next

        target_pos = self._count - (k % (self._count + 1))

        if target_pos < 0:
            dummy_tail.next.next = None
            dummy_head.next = None
            return head

        self._count = 0

        while self._count != target_pos:
            slow = slow.next
            self._count += 1

        head = slow.next
        slow.next = None
        return head