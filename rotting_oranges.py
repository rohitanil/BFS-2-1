"""
Time complexity -> O(M*N)
Space COmplexity -> O(M*N)

Logic:
Used BFS traversal. Initially, compute the total number of fresh oranges and insert to queue if an orange is rotten(row,col,curr_time). The initial
time for these oranges are set to 0 (curr_time)
Until the queue is empty, do BFS on the nodes and consider the neighbor oranges. We add them to the queue if they are fresh.
While doing that, we will decrement the fresh_orange count. This is done to check if we rot all the fresh oranges.
Here we are not using a visit_set to keep track of rows and cols we visited because we are changing the grid value from 1 to 2. So this
acts like an in place visit_set(This can be considered as a space optimization).

Finally return curr_time if fresh_oranges become 0 else -1 which means we werent able to rot some of the
oranges
"""
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        curr_time = 0
        neighbors = [
            [-1, 0], [1, 0],
            [0, -1], [0, 1]
        ]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append([r, c, curr_time])

        while queue:
            r, c, curr_time = queue.popleft()
            for del_row, del_col in neighbors:
                n_row, n_col = r + del_row, c + del_col
                if 0 <= n_row < ROWS and 0 <= n_col < COLS and grid[n_row][n_col] == 1:
                    grid[n_row][n_col] = 2
                    fresh_oranges -= 1
                    queue.append([n_row, n_col, curr_time + 1])

        return curr_time if fresh_oranges == 0 else -1
