from collections import defaultdict
import random


class Solution:

    def __init__(self, nums: list):
        self.num_dict = defaultdict(list)
        for i, num in enumerate(nums):
            self.num_dict[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.num_dict[target])