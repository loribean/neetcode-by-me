class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #perform binary search 
        low = 1
        high = max(piles)
        result = high

        while low <= high:
            mid = (low+high) // 2
            hours = getHoursForBananas(piles, mid,h)
            if hours > h:
                low = mid + 1
            elif hours <= h:
                high = mid -1
                if result > mid:
                    result = mid
        
        return result
            
            
    

def getHoursForBananas(piles: List[int], perHour: int, limit: h) -> int:
    hours = 0
    for item in piles:
           #get number of hours needed to complete the bananas
        hours += -(-item//perHour)
        if hours > limit: # Optimization: break early
                    break
    return hours