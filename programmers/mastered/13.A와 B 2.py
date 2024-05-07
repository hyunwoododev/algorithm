# https://www.acmicpc.net/problem/12919

START = list(input())
END = list(input())

def dfs(curr):
    if len(curr) < 1:
        return

    if curr == START:
        print(1)
        exit()  

    if curr[-1] == "A":
        copy = curr[:]
        copy.pop()
        dfs(copy)

    if curr[0] == "B":
        copy = curr[:]
        copy = copy[::-1]
        copy.pop()
        dfs(copy)

dfs(END)
print(0)




