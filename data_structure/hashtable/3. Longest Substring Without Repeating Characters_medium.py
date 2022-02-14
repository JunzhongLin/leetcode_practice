'''

Given a string s, find the length of the longest substring without repeating characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = collections.deque()
        hash_set = set()
        res = 0

        for cha in s:
            if cha in hash_set:
                res = max(res, len(queue))
                while cha in hash_set:
                    hash_set.remove(queue.popleft())

            queue.append(cha)
            hash_set.add(cha)

        res = max(res, len(queue))

        return res