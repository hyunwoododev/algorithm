from itertools import combinations

def solution(dots):
    for (x1, y1), (x2, y2), (x3, y3), (x4, y4) in combinations(dots, 4):
        if (y1 - y2) * (x3 - x4) == (y3 - y4) * (x1 - x2):
            return 1
    return 0
