class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset = []
        res = []
        

        def dfs(i):
            if i >= len(nums):
                return res.append(subset.copy())
            
            #decision where we add i
            subset.append(nums[i])
            dfs(i+1)
            #decision where we dont add i
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

        
                