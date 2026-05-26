class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        original = image[sr][sc]
        if original == color:
            return image # first base case
        rows, cols = len(image), len(image[0])

        def dfs(image,r,c):
            if (min(r, c) < 0 or # out of grid
                r == rows or c == cols or # out of grid
                image[r][c] != original): # node is not the original color
                return
            image[r][c] = color #color the node

            dfs(image, r + 1, c)
            dfs(image, r - 1, c)
            dfs(image, r, c + 1)
            dfs(image, r, c - 1)
        dfs(image, sr, sc)

        return image

        