"""
4375번문제

2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.
"""

"""
1. 외부 while 루프: 이 루프는 사용자로부터 계속해서 입력을 받기 위해 사용됩니다. 
try-except 블록을 통해 사용자가 잘못된 입력을 하거나 입력을 종료할 경우 (Ctrl+D 또는 파일의 끝에 도달하는 경우) 루프를 종료합니다.
이렇게 함으로써 여러 테스트 케이스를 연속으로 처리할 수 있습니다.

2. a = b%n 이고 b = c%n 이면 a = c%n 이다.
"""


while True:
    try:
        n = int(input())
    except:
        break

    number = 1
    count = 1

    while number % n != 0:
        number = number*10 + 1
        number %= n #이게 핵심임.
        count += 1

    print(count)

