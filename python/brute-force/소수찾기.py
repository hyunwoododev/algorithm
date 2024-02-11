from itertools import permutations

def isPrime(x):
    # 1과 자기 자신만을 약수로 갖는 수를 소수라고 합니다.
    # 따라서, 2 미만의 수는 소수가 아닙니다.
    if x < 2:
        return False
    
    # 2부터 x의 제곱근까지의 모든 수로 나누어보면서
    # x가 그 어떤 수로도 나누어 떨어지지 않는다면 소수입니다.
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    arr = []
    set_arr = []
    
    for i in range(1, len(numbers)+1):
        for per in permutations(numbers,i):
            arr.append(int("".join(per)))
            
    set_arr = list(set(arr))
    for item in set_arr:
        if isPrime(item):
            answer += 1
            
    return answer