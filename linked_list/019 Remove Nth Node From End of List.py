'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy

        while n!=0:
            fast=fast.next
            n -= 1
        while fast.next:
            slow=slow.next
            fast=fast.next

        slow.next = slow.next.next
        return dummy.next

    def removeNthFromEnd_TLE(self, head, n):
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp

        counts = 0
        cur = prev
        prev = None
        while cur:
            counts += 1
            if counts == n:
                temp = cur.next.next
                cur.next.next = prev

                prev = cur.next
                cur = temp
            else:
                temp = cur.next
                cur.next = prev

                prev = cur
                cur = temp
