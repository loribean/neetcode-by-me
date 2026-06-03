class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        #solve base with dp bottom up
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        prev_row = [0] * cols

        for r in range(rows - 1, -1, -1):
            curr_row = [0] * cols
            if obstacleGrid[r][cols-1] == 0:
                if r == rows -1:
                    curr_row[cols-1] = 1
                else:
                    curr_row[cols-1] = prev_row[cols-1]
            else:
                curr_row[cols-1] = 0

            for c in range(cols-2, -1, -1):
                if obstacleGrid[r][c] == 0:
                    curr_row[c] = curr_row[c + 1] + prev_row[c]
                else:
                    curr_row[c] = 0
            prev_row = curr_row
        return prev_row[0]


        