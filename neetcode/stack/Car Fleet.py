# https://leetcode.com/problems/car-fleet/description/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)

        for p,s in pairs: 
            time = (target - p) / s
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)

        return len(stack)
        

        