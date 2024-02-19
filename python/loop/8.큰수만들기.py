# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    # 첫 번째 숫자를 스택에 넣어 초기화합니다.
    stack = [number[0]]
    # 두 번째 숫자부터 순회를 시작합니다.
    for num in number[1:]:
        # 현재 스택이 비어 있지 않고, 스택의 마지막 요소가 현재 숫자보다 작으며,
        # 아직 제거할 숫자(k)가 남아 있는 동안 반복합니다.
        while stack and stack[-1] < num and k > 0:
            k -= 1            # 하나의 숫자를 제거했으므로 k를 1 감소시킵니다.
            stack.pop()       # 스택의 마지막 요소(가장 작은 숫자)를 제거합니다.
        
        # 현재 숫자를 스택에 추가합니다.
        stack.append(num)
    
    # 모든 숫자를 순회한 후에도 아직 제거할 숫자(k)가 남아 있다면,
    # 스택의 마지막부터 k개의 숫자를 제거합니다.
    if k != 0:
        stack = stack[:-k]
    
    # 스택에 남은 숫자들을 문자열로 합쳐서 반환합니다.
    return ''.join(stack)
