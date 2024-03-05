# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26 

        # 첫번째 윈도우 빈도수 계산
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        #  첫번째 윈도우의 같은 빈도수를 찾아서 몇개가 match되는지 탐색
        matches = 0 #-> 빈도수가 같은개 몇개인지.
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            # 현재 윈도우에서 빈도수가 같으면 permutation을 만들 수 있음.
            if matches == 26:
                return True

            # ------- 오른쪽 추가에 관한 로직 --------

            # 1. 추가되는 숫자의 index를 가져와서 빈도수를 더해줌.
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1

            # 2. 현재 빈도수가 같으니깐 matches를 1증가
            if s1Count[index] == s2Count[index]:
                matches += 1

            # 3. 현재 숫자를 하나 올림으로써 이제 더이상은 같지 않아진거기때문에 matches를 빼줘야함.
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # --------왼쪽을 제거하는 로직 --------# 

            # 4. 왼쪽에 제거되는 숫자의 index를 찾아서 빈도수를 제거함.
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1

            # 5. 현재 빈도수가 같으니깐 matches를 1증가
            if s1Count[index] == s2Count[index]:
                matches += 1
            # 6. 현재 숫자를 하나 빼줌으로써 이제 더이상은 같지 않아진거기때문에 matches를 빼줘야함.
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1
        return matches == 26
