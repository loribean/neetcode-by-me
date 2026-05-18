class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sumSet = []

        def dfs(i):

            total = sum(sumSet)

            if total == target:
                res.append(sumSet.copy())
                return
                
            if i >= len(nums) or total > target:
                return

            sumSet.append(nums[i])
            dfs(i)
            sumSet.pop()
            dfs(i+1)

        dfs(0)
        return res