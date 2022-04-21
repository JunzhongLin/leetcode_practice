'''

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
'''


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1

        t_table = [0] * (n + 1)
        t_table[0], t_table[1], t_table[2] = 0, 1, 1

        for i in range(3, n + 1):
            t_table[i] = t_table[i - 1] + t_table[i - 2] + t_table[i - 3]

        return t_table[-1]