from collections import defaultdict


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        letter_dict, ans = defaultdict(int), 0

        for l in s:
            letter_dict[l] += 1

        sorted_letter_dict = {k: v for (k, v) in sorted(letter_dict.items(), key=lambda item: item[1], reverse=True)}

        for i, key in enumerate(sorted_letter_dict):
            if i <= 8:
                ans += 1 * sorted_letter_dict[key]
            elif 8 < i <= 17:
                ans += 2 * sorted_letter_dict[key]
            else:
                ans += 3 * sorted_letter_dict[key]

        return ans