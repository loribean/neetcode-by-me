class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sumSet = []

        nums.sort()

        def dfs(i,total):

            if total == target:
                res.append(sumSet.copy())
                return

            if i >= len(nums) or total > target:
                return
            # DECISION TO ADD THIS NUMBER
            sumSet.append(nums[i])
            # DFS THE SAME NUMBER
            dfs(i,total + nums[i])
            # DECISION TO NOT ADD THIS NUMBER
            sumSet.pop()
            # DFS THE SAME NEXT NUM
            dfs(i+1, total)

        dfs(0,0)
        return res