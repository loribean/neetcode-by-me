class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #solve base with dp bottom up
        #If the start or destination cell has an obstacle, return 0 immediately.
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        #Create a 1D array dp of size cols, initialized to 0.
        prev_row = [0] * cols

        for r in range(rows - 1, -1, -1): #iterate backwards
            #Create a 1D array dp of size cols, initialized to 0.
            curr_row = [0] * cols
            #if theres no obstacles
            if obstacleGrid[r][cols-1] == 0:
                #& its the last row 
                if r == rows -1:
                    curr_row[cols-1] = 1 #theres 1 way to reach this point
                else:
                    curr_row[cols-1] = prev_row[cols-1] #else, we inherit the no of ways from the bottom
            #else, stays as 0 value if there is an obstacle
            for c in range(cols-2, -1, -1): #iterate backwards starting from second last
                if obstacleGrid[r][c] == 0:
                    curr_row[c] = curr_row[c + 1] + prev_row[c] # if not an obstacle, then we plus the bottom + right
                else:
                    curr_row[c] = 0 #its an obstacle
            prev_row = curr_row
        return prev_row[0] # we return the end res, first item in the grid


        