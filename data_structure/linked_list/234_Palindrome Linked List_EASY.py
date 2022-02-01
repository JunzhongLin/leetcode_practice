'''

Given the head of a singly linked list, return true if it is a palindrome.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp_list = []
        curr = head

        while curr is not None:
            temp_list.append(curr.val)
            curr = curr.next
        rev_temp_list = temp_list[:]
        rev_temp_list.reverse()
        # print(rev_temp_list)
        if temp_list == rev_temp_list:
            return True
        return False