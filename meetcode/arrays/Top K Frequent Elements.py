# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = sorted(count.items(), key=lambda x:x[1], reverse = True)
        return [x[0] for x in arr][0:k]