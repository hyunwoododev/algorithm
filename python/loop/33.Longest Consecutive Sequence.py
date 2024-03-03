# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 숫자 리스트를 오름차순으로 정렬합니다.
        nums.sort()

        # 'maxLength'와 'currentLength' 변수를 1로 초기화합니다.
        maxLength = 1
        currentLength = 1

        # 정렬된 배열을 두 번째 요소부터 반복하여 순회합니다.
        for i in range(1, len(nums)):
            # 현재 숫자가 이전 숫자와 다른지 확인합니다.
            if nums[i] != nums[i - 1]:
                # 현재 숫자가 이전 숫자보다 1 크면 연속적인 수열의 일부입니다.
                if nums[i] == nums[i - 1] + 1:
                    currentLength += 1
                else:
                    # 연속되지 않으면 현재 길이를 리셋합니다.
                    currentLength = 1

                # 최대 길이를 업데이트합니다.
                maxLength = max(maxLength, currentLength)

        # 최장 연속 수열의 길이인 'maxLength'를 반환합니다.
        return maxLength
