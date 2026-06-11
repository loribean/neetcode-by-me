class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start, end = 0, len(numbers) -1

        while start < end:
            currentSum = numbers[start] + numbers[end]
            if currentSum < target:
                start += 1
            elif currentSum > target:
                end -= 1
            else:
                return [start+1, end+1]

        return []

        