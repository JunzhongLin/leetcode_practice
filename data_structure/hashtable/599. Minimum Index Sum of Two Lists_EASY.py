'''

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
'''


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        map_list1 = {}
        score_map = collections.defaultdict(list)
        min_score = len(list1) + len(list2) - 2

        for index, item in enumerate(list1):
            map_list1[item] = index

        for index, item in enumerate(list2):
            if item in map_list1:
                score = map_list1[item] + index
                min_score = min(min_score, score)
                score_map[score].append(item)

        return score_map[min_score]