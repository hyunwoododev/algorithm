# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        # 1. nums를 세 리스트로 분리: 음수, 양수, 0
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. O(1) 조회 시간을 위해 음수와 양수를 별도의 집합으로 생성
        N, P = set(n), set(p)

        # 3. 리스트에 0이 최소 한 개 있는 경우, N에서 -num이 있고 P에서 num이 있는 모든 경우를 추가
        #    예: (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        # 4. 리스트에 0이 적어도 세 개 이상 있는 경우, (0, 0, 0) = 0도 포함
        if len(z) >= 3:
            res.add((0, 0, 0))

        # 5. 모든 음수 쌍에 대하여, 그들의 합의 보수(양수)가 양수 집합에 있는지 확인
        #    예: (-3, -1)의 보수는 4
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # 6. 모든 양수 쌍에 대하여, 그들의 합의 보수(음수)가 음수 집합에 있는지 확인
        #    예: (1, 1)의 보수는 -2
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res
