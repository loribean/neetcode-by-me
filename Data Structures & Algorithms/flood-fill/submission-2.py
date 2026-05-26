class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        original = image[sr][sc]
        if original == color:
            return image
        rows, cols = len(image), len(image[0])

        def dfs(image,r,c,visit, original):
            if (min(r, c) < 0 or
                r == rows or c == cols or
                (r,c) in visit or image[r][c] != original):
                return
            if image[r][c] == original:
                image[r][c] = color
            
            visit.add((r,c))

            dfs(image, r + 1, c, visit,original)
            dfs(image, r - 1, c,visit, original)
            dfs(image, r, c + 1,visit,original)
            dfs(image, r, c - 1,visit,original)

            visit.remove((r,c))
        dfs(image, sr, sc,set(), original)

        return image

        