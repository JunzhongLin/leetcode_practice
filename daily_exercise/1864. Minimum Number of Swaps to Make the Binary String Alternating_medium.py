class Solution:
    def minSwaps(self, s: str) -> int:
        zeros, ones, diffs, diffs_swap = 0, 0, 0, 0

        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            else:
                zeros += 1

        if abs(zeros - ones) > 1:
            return -1

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0' and ones > zeros:
                    diffs += 1
                elif s[i] == '1' and zeros > ones:
                    diffs += 1

                elif s[0] == '0' and zeros == ones and s[i] == '1':
                    diffs += 1
                elif s[0] == '1' and zeros == ones and s[i] == '0':
                    diffs += 1

                elif s[0] == '0' and zeros == ones and s[i] == '0':
                    diffs_swap += 1
                elif s[0] == '1' and zeros == ones and s[i] == '1':
                    diffs_swap += 1

            # elif i%2 == 1:
            #     if s[i] == '0' and ones < zeros:
            #         diffs += 1
            #     elif s[i] == '1' and zeros < ones:
            #         diffs += 1
            #     elif s[0] == '1' and zeros == ones and s[i]=='1':
            #         diffs += 1
            #     elif s[0] == '0' and zeros == ones and s[i]=='0':
            #         diffs += 1
            #     elif s[0] == '1' and zeros == ones and s[i]=='0':
            #         diffs_swap += 1
            #     elif s[0] == '0' and zeros == ones and s[i]=='1':
            #         diffs_swap += 1

        return int(diffs) if zeros != ones else min(int(diffs), int(diffs_swap))