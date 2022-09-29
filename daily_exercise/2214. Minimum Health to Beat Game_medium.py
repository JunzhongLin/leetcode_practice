from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        ans = 0
        max_attack = max(damage) # n = len(damage), O(n)

        total_damage = sum(damage) - max_attack + max_attack - armor if armor < max_attack else sum(damage) - max_attack
        # O(n)

        return total_damage + 1  # 2*O(n)