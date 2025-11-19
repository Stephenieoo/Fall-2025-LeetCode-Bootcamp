from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use defaultdict saves me from repeatedly checking whether a key already exists before appending to it
        graph = defaultdict(list)

        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque()
        # all courses with indegree 0 append to q
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []
        while q:
            course = q.popleft()
            order.append(course)
            # its neighboring courses nxt are one step closer to being available
            for nxt in graph[course]:
                # reduce the indegree of each neighbor
                indegree[nxt] -= 1
                # when 
                if indegree[nxt] == 0:
                    q.append(nxt)
        return order if len(order) == numCourses else []