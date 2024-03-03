# # https://www.acmicpc.net/problem/15903
# # solved!
# import heapq

# n,m = map(int,input().split())
# n_list = list(map(int,input().split()))
# heapq.heapify(n_list)
# for _ in range(m):
# 	a = heapq.heappop(n_list)
# 	b = heapq.heappop(n_list)
# 	heapq.heappush(n_list,a+b)
# 	heapq.heappush(n_list,a+b)
# print(sum(n_list))



    




