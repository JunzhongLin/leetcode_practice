class Solution:
    def wordBreak_iter(self, s: str, wordDict: List[str]) -> bool:
        stack = [s]
        word_set = set(wordDict)
        max_len_word = len(sorted(wordDict, key=lambda x: len(x))[-1])
        visited = set()

        while stack:
            candidate = stack.pop()

            for i in range(len(candidate)):
                if candidate[:i + 1] in word_set and i + 1 <= max_len_word:
                    if len(candidate[i + 1:]) == 0:
                        return True
                    elif candidate[i + 1:] in visited:
                        continue
                    stack.append(candidate[i + 1:])
                    visited.add(candidate[i + 1:])
                elif i + 1 > max_len_word:
                    break
        return False

    def wordBreak_td(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)
        max_len_word = len(sorted(wordDict, key=lambda x: len(x))[-1])

        @lru_cache(maxsize=None)
        def dp(ind):
            if ind == -1:
                return True
            elif ind < -1:
                return False

            for i in range(ind, ind - max_len_word, -1):
                if s[i:ind + 1] in word_set and dp(i - 1):
                    return True

            return False

        return dp(len(s) - 1)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        word_set = set(wordDict)
        max_len_word = len(sorted(wordDict, key=lambda x: len(x))[-1])

        for i in range(1, len(s) + 1):
            for j in range(1, max_len_word + 1):
                if i + j - 1 > len(dp) - 1:
                    continue

                if s[i - 1:i + j - 1] in word_set and dp[i - 1]:
                    dp[i + j - 1] = True

        return dp[-1]