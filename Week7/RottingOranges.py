from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # essentially a spread/propagation problem ona grid
        m = len(grid)
        n = len(grid[0])
        f = 0
        q = deque()
        # append all rotting oranges to the queue, count the number of fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    f += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        # if no fresh initially
        if f == 0:
            return 0
        # define four directions
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        # bfs traversal
        res = 0
        while q and f != 0:
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()
                for (dr, dc) in dirs:
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        f -= 1
            res += 1
        return res if f == 0 else -1