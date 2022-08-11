from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        res, remained_size = 0, truckSize

        for box_type in boxTypes:

            if box_type[0] < remained_size:
                remained_size -= box_type[0]
                res += box_type[0] * box_type[1]

            else:
                res += remained_size * box_type[1]
                break

        return res