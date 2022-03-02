'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists_iter(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        prev = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next

            else:
                prev.next = list2
                list2 = list2.next

            prev = prev.next

        prev.next = list1 if list1 is not None else list2

        return dummy.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        prev = dummy

        def helper(node1, node2, prev):
            if not node2:
                prev.next = node1
                return None
            elif not node1:
                prev.next = node2
                return None

            elif node1.val < node2.val:
                prev.next = node1
                node1 = node1.next
                # print(dummy.next)
            else:
                prev.next = node2
                node2 = node2.next
                # print(dummy.next)

            prev = prev.next
            helper(node1, node2, prev)

        helper(list1, list2, prev)

        return dummy.next