# https://www.hackerrank.com/challenges/missing-numbers/problem

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    m = int(input())
    B = [int(i) for i in input().split()]

    vals = {}

    for i in A:
        if i not in vals:
            vals[i] = -1
        else:
            vals[i] -= 1

    for i in B:
        if i not in vals:
            vals[i] = 1
        else:
            vals[i] += 1

    pos = []
    for i in vals: # 딕셔니리를 for문 돌리는 개충격적인 사실 ..
        if vals[i] > 0:
            pos.append(i)
            
    pos.sort()
    for i in pos:
        print(i,end=' ')