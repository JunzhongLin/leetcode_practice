# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        dummy_head = ListNode()
        dummy_head.next = head
        length_list = 0
        while head:
            length_list += 1
            head = head.next

        head = dummy_head.next

        def merge_sort(head, length_list):
            if length_list == 1:
                return head

            head_a = head
            pivot = length_list // 2
            prev, curr = None, head
            while pivot > 0:
                prev, curr = curr, curr.next
                pivot -= 1
            prev.next = None
            head_b = curr
            length_a, length_b = length_list // 2, length_list - length_list // 2
            head_a_sorted, head_b_sorted = merge_sort(head_a, length_a), merge_sort(head_b, length_b)
            return self.merge(head_a_sorted, head_b_sorted)

        return merge_sort(head, length_list)

    def merge(self, head_a, head_b):
        dummy = ListNode()
        if head_a.val <= head_b.val:
            dummy.next = head_a
            curr_a, curr_b = head_a.next, head_b
        else:
            dummy.next = head_b
            curr_a, curr_b = head_a, head_b.next

        curr = dummy.next

        while curr_a and curr_b:
            if curr_a.val >= curr_b.val:
                curr.next, curr_b = curr_b, curr_b.next
            else:
                curr.next, curr_a = curr_a, curr_a.next
            curr = curr.next

        if curr_a:
            curr.next = curr_a
        else:
            curr.next = curr_b

        return dummy.next