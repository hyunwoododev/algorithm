# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 스택과 결과를 저장할 리스트를 초기화합니다.
        stack = []
        res = []

        # 백트래킹 함수를 정의합니다. openN과 closedN은 각각 지금까지 추가된 여는 괄호와 닫는 괄호의 수를 나타냅니다.
        def backtrack(openN, closedN):
            # 만약 여는 괄호와 닫는 괄호의 수가 모두 n에 도달했다면, 현재까지의 조합을 결과 리스트에 추가합니다.
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # 여는 괄호의 수가 n보다 작다면, 여는 괄호를 추가하고 재귀 호출합니다.
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()  # 재귀 호출이 끝나면, 마지막으로 추가한 괄호를 제거하여 이전 상태로 되돌립니다.
                
            # 닫는 괄호의 수가 현재 여는 괄호의 수보다 작다면, 닫는 괄호를 추가하고 재귀 호출합니다.
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()  # 마찬가지로 재귀 호출 후에는 마지막으로 추가한 괄호를 제거합니다.

        # 백트래킹을 시작합니다. 처음에는 여는 괄호와 닫는 괄호의 수 모두 0입니다.
        backtrack(0, 0)
        # 모든 가능한 괄호 조합이 저장된 결과 리스트를 반환합니다.
        return res

