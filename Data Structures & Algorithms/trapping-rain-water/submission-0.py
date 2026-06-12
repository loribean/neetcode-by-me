class Solution:
    def trap(self, height: List[int]) -> int:
        #to find the rainwater trapped at any point,
        #we need to find the min of two points, the max of the left and right of each point
        #then we need to minus of the current area of the point

        #brute force, we can go to each point and calculate the min of the max
        # but thats ON^2
        # Alternatively, 
        # 1. we can calculate make two passes to calculate the max of left and right, suffix and prefix, but this will take 03n space
        # 2. OR, most optimally, we can use two pointers O(N) time and O(1) space
        # 2. Since water at any point depends on shorter wall, we keep track of highest wall seen on each side.
        # 2. Water will be simply - max wall on that side - height at that position


        if not height:
            return 0

        l,r = 0, len(height) -1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res