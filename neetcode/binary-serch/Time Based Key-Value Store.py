# https://leetcode.com/problems/time-based-key-value-store/description/

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeHash = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeHash[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        allList = self.timeHash[key]
        ans = ""
        
        if not allList or allList[0][0] > timestamp:
            return ans

        l = 0
        r = len(allList) - 1  
        while l <= r:
            mid = (l+r) // 2
            stamp, value = allList[mid]   
            if stamp == timestamp:
                return value

            if stamp > timestamp:
                r = mid - 1

            else:
                ans = allList[mid][1]
                l = mid + 1

        return ans
