'''
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed
'''

from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products = sorted(products)
        res = []

        filtered_list = products
        for idx, cha in enumerate(searchWord):
            matched = []
            for p in filtered_list:
                if len(p) <= idx:
                    continue

                if p[idx] == cha:
                    matched.append(p)

            if len(matched) >= 3:
                res.append(matched[:3])
            else:
                res.append(matched)

            filtered_list = matched

        return res