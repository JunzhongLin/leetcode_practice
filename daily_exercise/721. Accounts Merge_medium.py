class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        visited_accounts = [False] * len(accounts)
        res = []
        accounts_dict = defaultdict(list)

        for i, account in enumerate(accounts):
            for email in account[1:]:
                accounts_dict[email].append(i)

        def dfs(idx, emails):

            if visited_accounts[idx]:
                return None
            visited_accounts[idx] = True

            for email in accounts[idx][1:]:
                emails.add(email)
                for i in accounts_dict[email]:
                    dfs(i, emails)

        for i in range(len(accounts)):
            if visited_accounts[i]:
                continue
            name = accounts[i][0]
            emails = set()

            dfs(i, emails)

            res.append([name] + sorted(emails))

        return res