class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        #use binary search to find out if value exists within array
        #if it doesnt exist, find the next smallest item in the array based on timestamp
        res = ""
        values = self.store.get(key, [])
        
        #binary search

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            proposed = values[m]
            p_time = proposed[1]
            if p_time < timestamp:
                l = m+1
                res = proposed[0]
            elif p_time > timestamp:
                r = m - 1
            else: 
                return proposed[0]
        return res
            
        

