# https://www.acmicpc.net/problem/1541
# solved!
n = input()
answer = 0
arr = n.split("-")
plus_arr = arr[0].split("+")
minus_arr = arr[1:]
for i in plus_arr:
    answer += int(i)

for subarr in minus_arr:
    subarr = subarr.split("+")
    for j in subarr:
        answer-=int(j)
print(answer)