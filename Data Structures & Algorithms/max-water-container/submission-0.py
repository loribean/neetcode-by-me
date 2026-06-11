class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            left_height, right_height = heights[l],heights[r]
            height = min(left_height, right_height)
            width = r-l
            area = height * width
            res = max(area, res)

            if left_height <= right_height:
                l += 1
            else:
                r -= 1

        return res