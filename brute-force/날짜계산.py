# 문제 :
# 우리는 사람이 태어나면 1년 만에 1의 나이를 가진다. 2년 후에는 2의 나이를 가진다. 따라서 n년 후에는 n의 나이를 갖게 된다. 어떤 나라에는 수 3개를 이용해서 연도를 나타낸다. 각각의 수는 지구, 태양, 그리고 달을 나타낸다.
# 지구를 나타내는 수를 E, 태양을 나타내는 수를 S, 달을 나타내는 수를 M이라고 했을 때, 이 세 수는 서로 다른 범위를 가진다. (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
# 우리가 알고 있는 1년은 준규가 살아있는 나라에서는 1 1 1로 나타낼 수 있다. 1년이 지나면, 세 수는 모두 1씩 증가한다. 만약, 어떤 수가 범위를 넘어가는 경우에는 1이 된다.
# 예를 들어, 15년은 15 15 15로 나타낼 수 있다. 하지만, 1년 후에는 1 16 16이 된다.
# E, S, M으로 현재 연도를 나타낸 수가 주어졌을 때, 가장 처음 연도를 구하는 프로그램을 작성하시오.

# 풀이 :
# 입력으로 주어진 E, S, M을 받는다.
# 연도를 1로 초기화하고, 반복문을 통해 연도를 1씩 증가시킨다.
# 연도(year)를 15, 28, 19로 각각 나눈 나머지 값이 E, S, M과 일치하는지 확인한다.
# 만약 일치한다면 해당 연도를 출력하고 반복문을 종료한다.

E, S, M = map(int, input().split())
year = 1
while True:
    if year % 15 == (E % 15) and year % 28 == (S % 28) and year % 19 == (M % 19):
        print(year)
        break
    year += 1
