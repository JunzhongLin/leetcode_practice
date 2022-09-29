from typing import List
import bisect

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        candles_list, ans, i = [], [], 0

        for i, cha in enumerate(s):
            if cha == '|':
                candles_list.append(i)
        print(candles_list)

        if len(candles_list) < 2:
            return [0] * len(queries)

        for query in queries:

            left, right = 0, len(candles_list) - 1
            left_candle, right_candle = None, None

            if candles_list[left] >= query[1] or candles_list[right] <= query[0]:
                ans.append(0)
                continue

            while right - left > 0:
                mid = (left + right) // 2

                if candles_list[mid] > query[0]:
                    right = mid
                elif candles_list[mid] < query[0]:
                    left = mid + 1
                else:
                    break
                print(left, right)

            print(candles_list[(left + right) // 2], (left + right) // 2, left, right)
            if query[1] > candles_list[(left + right) // 2] >= query[0]:
                left_candle, candle_index_left = candles_list[(left + right) // 2], (left + right) // 2

            left, right = 0, len(candles_list)-1

            while right - left > 0:
                mid = (left + right)//2 + 1

                if candles_list[mid] > query[1]:
                    right = mid - 1
                elif candles_list[mid] < query[1]:
                    left = mid
                else:
                    break

            if left != right:
                mid = (left+right)//2+1
            else:
                mid = left

            if query[0] < candles_list[mid] <= query[1]:
                right_candle, candle_index_right = candles_list[mid], mid

            print(left_candle, right_candle)
            if left_candle is not None and right_candle is not None:
                ans.append(right_candle - left_candle + 1 - (candle_index_right - candle_index_left + 1))
            else:
                ans.append(0)

        return ans

    def platesBetweenCandles_bisect(self, s, queries):
        A = [i for i,c in enumerate(s) if c == '|']
        res = []
        for a,b in queries:
            i = bisect.bisect_left(A, a)
            j = bisect.bisect(A, b) - 1
            res.append((A[j] - A[i]) - (j - i) if i < j else 0)
        return res


a="|||||*|||*|||*||||*||||**|*|||**|**||**|||*|||*||***||*|*||"
queries = [[0, 56]]

res=Solution().platesBetweenCandles(a, queries)