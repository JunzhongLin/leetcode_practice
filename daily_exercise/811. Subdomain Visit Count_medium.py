from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        domains_dict, res = defaultdict(int), []

        for cpdomain in cpdomains:
            end_idx_count = cpdomain.find(' ')
            count = int(cpdomain[:end_idx_count])
            cpdomain = cpdomain[end_idx_count + 1:]

            while len(cpdomain) != 0:
                domains_dict[cpdomain] += count
                if not cpdomain.__contains__('.'):
                    break
                cpdomain = cpdomain[cpdomain.find('.') + 1:]

        for key in domains_dict.keys():
            res.append(' '.join([str(domains_dict[key]), key]))

        return res