class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #essentially this is a bfs question
        #go layer by layer in order to spread the rotting fruit

        rows, cols = len(grid), len(grid[0])
        visit = set()
        fresh_fruits = set()
        queue = deque()

        time = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visit.add((i,j))
                if grid[i][j] == 1:
                    fresh_fruits.add((i,j))
        if not fresh_fruits:
            return time

        while queue and fresh_fruits:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                neighbors = [[0,1],[1,0], [-1,0], [0, -1]]

                for dr, dc in neighbors:
                    res_r, res_c = r + dr, c + dc

                    if (min(res_r, res_c) < 0 or
                        res_r == rows or res_c == cols or
                        (res_r, res_c) in visit or grid[res_r][res_c] == 0):
                        continue
                    fresh_fruits.discard((res_r, res_c))
                    queue.append((res_r, res_c))
                    visit.add((res_r, res_c))
            time += 1

        if fresh_fruits:
            return -1
        else:
            return time
                    
