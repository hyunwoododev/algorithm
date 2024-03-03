# # https://www.acmicpc.net/problem/10610

n = sorted(list(input()), reverse=True)
sum = sum(map(int, n))
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))

# N = input()

# if '0' not in N:
#     print(-1)
#     exit()
# sum = 0
# for i in N:
#     sum += int(i)
# if sum % 3 != 0:
#     print(-1)
#     exit()    

# N = sorted(N)
# print("".join(N[::-1]))



