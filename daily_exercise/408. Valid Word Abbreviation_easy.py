class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        slow, fast = 0, 0
        digits_set = {d for d in list('0123456789')}
        temp_list = []

        while slow < len(abbr) and fast < len(abbr):
            if abbr[fast] not in digits_set and slow == fast:
                temp_list.append(abbr[fast])
                fast += 1
                slow = fast

            elif abbr[fast] in digits_set:
                fast += 1

            else:
                if abbr[slow] == '0':
                    return False
                temp_list.append(int(abbr[slow:fast]))
                slow = fast

        if slow != fast:
            if abbr[slow] == '0':
                return False
            temp_list.append(int(abbr[slow:fast]))

        i = 0

        for abb in temp_list:
            if i > len(word):
                return False
            elif type(abb) == str:
                if i < len(word) and abb == word[i]:
                    i += 1
                else:
                    return False
            elif type(abb) == int:
                i += abb

        if i == len(word):
            return True
        else:
            return False