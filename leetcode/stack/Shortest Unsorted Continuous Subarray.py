# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        l, u = len(nums) - 1, 0  # l은 배열의 왼쪽 경계를, u는 배열의 오른쪽 경계를 의미
        stack = []  # 스택 초기화
        
        # 왼쪽부터 시작해서 정렬이 깨지는 지점 찾기
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:  # 현재 숫자가 스택의 top보다 작다면
                l = min(l, stack.pop())  # 스택을 pop하고 l을 업데이트
            stack.append(i)  # 현재 인덱스를 스택에 추가
        
        stack = []  # 스택 초기화
        
        # 오른쪽부터 시작해서 정렬이 깨지는 지점 찾기
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:  # 현재 숫자가 스택의 top보다 크다면
                u = max(u, stack.pop())  # 스택을 pop하고 u를 업데이트
            stack.append(i)  # 현재 인덱스를 스택에 추가
        
        # l이 u보다 크거나 같으면 이미 정렬된 배열이므로 0 반환
        # 그렇지 않으면 u - l + 1을 반환하여 정렬이 필요한 부분 배열의 길이를 구함
        return 0 if l >= u else u - l + 1
