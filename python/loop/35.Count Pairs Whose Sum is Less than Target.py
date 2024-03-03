# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()  # 리스트를 오름차순으로 정렬합니다.
        count = 0  # 조건을 만족하는 쌍의 수를 세는 변수입니다.
        left, right = 0, len(nums) - 1  # 'left'는 리스트의 시작 부분을, 'right'는 끝 부분을 가리킵니다.

        while left < right:  # 'left' 인덱스가 'right' 인덱스보다 작은 동안 반복합니다.
            if nums[left] + nums[right] < target:  # 두 수의 합이 타겟보다 작으면,
                count += right - left  # 'right'와 'left' 사이에 있는 숫자의 개수를 카운트에 더합니다.
                left += 1  # 'left' 인덱스를 오른쪽으로 이동시킵니다.
            else:  # 두 수의 합이 타겟보다 크거나 같으면,
                right -= 1  # 'right' 인덱스를 왼쪽으로 이동시킵니다.

        return count  # 조건을 만족하는 쌍의 총 수를 반환합니다.
