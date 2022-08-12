from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = []

        course_left = set([i for i in range(numCourses)])
        req_dict, set_req, learned_set = defaultdict(list), set(), set()
        for req in prerequisites:
            req_dict[req[0]].append(req[1])
            set_req.add(req[0])

        start_course = course_left - set_req

        if len(start_course) == 0:
            return []

        que = list(start_course)

        while que:
            for i in range(len(que)):
                course = que.pop(0)
                res.append(course)
                if course in course_left:
                    course_left.remove(course)
                learned_set.add(course)

            for course in list(req_dict):
                if set(req_dict[course]).issubset(learned_set):
                    req_dict.pop(course)
                    que.append(course)

        if len(course_left) == 0:
            return res
        else:
            return []