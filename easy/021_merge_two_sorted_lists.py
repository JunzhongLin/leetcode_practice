#  将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#  示例：
#
#  输入：1->2->4, 1->3->4
#  输出：1->1->2->3->4->4
from itertools import groupby


class ListNode:
    def __init__(self, x):
        self.val = x  # value
        self.next = None  # next pointer, record of location of next node


class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        l = ListNode(None)  # new list
        temp = l  # keep the location of the current last node

        while l1 != None and l2 != None:
            # while none of the two remaining lists is empty, keep going
            if l1.val <= l2.val:
                # when the value in l1's head node is less than
                # that in l2's,
                # put it in the new list
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                # else put that in l2's head node in new list
                temp.next = l2
                l2 = l2.next
                temp = temp.next

        # going out of the loop, put the rest of l1 or l2 in new list
        if l1 == None:
            temp.next = l2
        else:
            temp.next = l1

        return l.next


