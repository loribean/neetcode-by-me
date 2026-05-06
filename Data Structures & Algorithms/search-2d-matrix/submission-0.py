class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

    # given a matrix
    # 1,2,3,4,5
    # 6,7,8,9,10
    # 11,12,13,14,15
    # 16,17,18,19,20

    #what we need to do is do nested binary search
    #first lets search through the first number of each list
    #if target is with that range, then we look at the list

        rows, cols = len(matrix), len(matrix[0])
        #top is first item of first array, bottom is first item of last array
        top, bottom = 0, rows-1

        while top <= bottom:
            #make a guess, make it the middle
            row = (top+bottom) // 2
            
            #if the target is more than the last item of the middle row
            if target > matrix[row][-1]:
            # then the next iteration, the lower bound will be increased
                top = row + 1
            #if the target is less than the first item of the middle row
            elif target < matrix[row][0]:
                #then the next iteration, the upper bound will be decreased
                bottom = row - 1
            else:
            #if target is less than the last item of the middle row
            # and the item is more the the first item in the middle row
            # we got the correct row!
                break
        if not (top <= bottom):
        #if top is more than bottom, the pointers have crossed and target doesnt exist
            return False
        row = (top + bottom) // 2
        left,right = 0, cols -1 # left is first index of row, right is last index of row

        while left <= right:
            mid = (left+right) //2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False

