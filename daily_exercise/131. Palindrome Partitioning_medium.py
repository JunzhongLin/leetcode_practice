class Solution:
    def partition_find_all_paralindrome_subsets(self, s: str) -> List[List[str]]:

        res = set()
        n = len(s)
        que = [(i, i) for i in range(len(s))]

        while que:
            left, right = que.pop(0)

            res.add(s[left:right + 1])
            if left - 1 >= 0 and right + 1 <= n - 1 and s[left - 1] == s[right + 1]:
                que.append((left - 1, right + 1))

            if left == right and right + 1 <= n - 1 and s[left] == s[right + 1]:
                que.append((left, right + 1))

        return list(res)

    def partition(self, s: str) -> List[List[str]]:

        res, n, records = [], len(s), set()

        que = [[(i, i) for i in range(n)]]

        while que:
            tmp = que.pop(0)
            partition = [s[i:j + 1] for (i, j) in tmp]
            if tuple(tmp) in records:
                continue

            res.append(partition)
            records.add(tuple(tmp))

            for k, (i, j) in enumerate(tmp):

                if i == j and j + 1 <= n - 1 and tmp[k + 1][0] == tmp[k + 1][1] and s[j + 1] == s[j]:
                    tmp_res = tmp[:k]
                    tmp_res.append((i, j + 1))
                    tmp_res.extend(tmp[k + 2:])
                    que.append(tmp_res)

                if i - 1 >= 0 and j + 1 <= n - 1 and tmp[k - 1][0] == tmp[k - 1][1] and tmp[k + 1][0] == tmp[k + 1][
                    1] and s[i - 1] == s[j + 1]:
                    tmp_res = tmp[:k - 1]
                    tmp_res.append((i - 1, j + 1))
                    tmp_res.extend(tmp[k + 2:])
                    que.append(tmp_res)

        return res