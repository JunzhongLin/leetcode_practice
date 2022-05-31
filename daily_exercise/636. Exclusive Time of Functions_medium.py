class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        curr_time = 0
        for log in logs:
            l, r = log.find(':'), log.rfind(':')
            id_, status, time = int(log[:l]), log[l + 1:r], int(log[r + 1:])
            if status == 'start':
                if stack != []:
                    res[stack[-1][0]] += time - curr_time

                stack.append((id_, status, time))
                curr_time = time

            elif status == 'end':
                # print(res, stack)
                res[stack[-1][0]] += time + 1 - curr_time
                curr_time = time + 1
                stack.pop()

        return res