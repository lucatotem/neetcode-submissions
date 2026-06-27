from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        predic = defaultdict(list)
        for course in prerequisites:
            predic[course[1]].append(course[0])

        passed = set()

        def dfs(crs):
            if crs in passed:
                return False
            if predic[crs] == []:
                return True
            passed.add(crs)
            for pre in predic[crs]:
                if not dfs(pre):
                    return False
            passed.remove(crs)
            predic[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        

            