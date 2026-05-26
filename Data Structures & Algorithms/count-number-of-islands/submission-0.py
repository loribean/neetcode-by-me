class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            if (min(r,c) < 0 or
                r == rows or c == cols or
                grid[r][c] == "0"):
                return

            grid[r][c] = "0" # mark as "visited"
            for dr, dc in directions:
                dfs(r + dr, c + dc) #dfs all 4 directions

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # only the original first foot of island gets to remain as 1
                    dfs(r, c)
                    islands += 1
        return islands


        