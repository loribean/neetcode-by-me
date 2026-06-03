class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))

        length = 1

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == rows - 1 and c == cols - 1: #base case 1 => reached the end
                    return length
                neighbours = [[0,1], [0,-1], [1,0], [-1,0], [-1,1], [1,1], [1,-1], [-1,-1]]

                for dr, dc in neighbours:
                    res_row, res_col = r + dr, c + dc
                    if (min(res_row, res_col) < 0 or
                        res_row == rows or res_col == cols or 
                        (res_row, res_col) in visit or grid[res_row][res_col] == 1):
                        continue
                    queue.append((res_row, res_col))
                    visit.add((res_row, res_col))
            length += 1

        return -1
