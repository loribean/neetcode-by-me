class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #use dp to solve this problem.
        #we can use bottom up to solve
        #each grid, its answer is the sum of its right & bottom
        prev_row = [1] * n
        for r in range(m -2 , -1, -1): # move backward
            curr_row = [0] * n
            curr_row[n-1] = 1 # last item of each row, there only 1 way 

            for c in range(n -2, -1,-1): # move backward from second last item
                curr_row[c] = curr_row[c+1] + prev_row[c]
            prev_row = curr_row

        return prev_row[0]
        