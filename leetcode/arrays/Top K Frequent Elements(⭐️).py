# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        # num count
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        counter = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        return [n for n, c in counter][0:k]