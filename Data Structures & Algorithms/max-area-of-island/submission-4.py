class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            #out of grid
            if (min(r,c) < 0 or
                r == rows or c == cols or
                grid[r][c] == 0 or
                (r, c) in visit):# we hit water
                return 0
            visit.add((r, c)) # do something here
            
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        max_size = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_size = max(max_size, dfs(r, c))

        return max_size

