# https://leetcode.com/problems/trapping-rain-water/description/
# ⭐️

class Solution:
    def trap(self, height: List[int]) -> int:
        # 높이 배열이 비어있으면 저장할 빗물이 없으므로 0을 반환합니다.
        if not height:
            return 0

        # 양 끝에서 시작하는 두 포인터 l(왼쪽), r(오른쪽)를 초기화합니다.
        l, r = 0, len(height) - 1
        # 각 방향에서의 최대 높이를 저장할 변수를 초기화합니다.
        leftMax, rightMax = height[l], height[r]
        # 결과값을 저장할 변수입니다.
        res = 0
        # 왼쪽 포인터가 오른쪽 포인터보다 작은 동안 반복합니다.
        while l < r:
            # 왼쪽 최대 높이가 오른쪽 최대 높이보다 작은 경우
            if leftMax < rightMax:
                # 왼쪽 포인터를 오른쪽으로 이동시킵니다.
                l += 1
                # 새로운 위치에서의 최대 높이를 갱신합니다.
                leftMax = max(leftMax, height[l])
                # 현재 위치에서 저장할 수 있는 빗물의 양을 계산하여 결과에 추가합니다.
                res += leftMax - height[l]
            else:
                # 오른쪽 포인터를 왼쪽으로 이동시킵니다.
                r -= 1
                # 새로운 위치에서의 최대 높이를 갱신합니다.
                rightMax = max(rightMax, height[r])
                # 현재 위치에서 저장할 수 있는 빗물의 양을 계산하여 결과에 추가합니다.
                res += rightMax - height[r]
        # 계산된 결과를 반환합니다.
        return res

