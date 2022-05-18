class Solution:
    def simplifyPath(self, path: str) -> str:
        slow, fast = 0, 1
        path_list = []

        while slow < len(path) - 1:

            if fast < len(path) and path[fast] != '/':
                fast += 1

            else:
                if slow + 1 < fast:
                    path_list.append(path[slow + 1:fast])

                    if path_list[-1] == '..':
                        if len(path_list) >= 2:
                            path_list.pop()
                            path_list.pop()
                        else:
                            path_list.pop()

                    elif path_list[-1] == '.':
                        path_list.pop()

                slow = fast
                fast += 1

        return '/' + '/'.join(path_list)