# https://www.acmicpc.net/problem/1700
# 입력: n은 멀티탭 구멍의 수, k는 전기 용품 사용 횟수
n, k = map(int,input().strip().split())
items = list(map(int,input().split()))

# 멀티탭 초기 상태 설정: n개의 구멍이 모두 비어있음을 나타냄
multiTap = [0] * n
cnt=0  # 플러그를 뽑는 횟수를 세는 변수

for i in range(len(items)):
    # 현재 전기 용품이 이미 멀티탭에 꽂혀있으면, 그대로 둔다
    if items[i] in multiTap:
          continue
    else:
      # 멀티탭에 빈 구멍이 있으면, 그곳에 현재 전기 용품을 꽂는다
      if 0 in multiTap:
          multiTap[multiTap.index(0)] = items[i]
      else:
        # 멀티탭이 모두 차 있을 때의 처리 로직
        # 현재 위치 이후로 멀티탭에 꼽혀 있으며, 다시 사용될 전기 용품들의 목록을 생성
        appear = []
        for j in range(i+1,len(items)):
            if items[j] in multiTap:
                appear.append(items[j])
        
        if(appear):
          # 중복을 제거하고 순서를 유지하기 위해 사전(dict)을 사용하여 리스트를 다시 생성
          result_list = list(dict.fromkeys(appear))
          for k in range(len(multiTap)):
            # 다시 사용되지 않는 전기 용품이 있으면 그것을 뽑는다
            if multiTap[k] not in result_list:
                  multiTap[k]=items[i]
                  cnt+=1
                  break
          else:
            # 모든 멀티탭에 꽂힌 전기 용품이 나중에 다시 사용되면, 가장 나중에 사용될 용품을 뽑는다
            multiTap[multiTap.index(result_list[-1])]=items[i]
            cnt+=1
        else:
          # 멀티탭에 꽂힌 모든 전기 용품이 다시 사용되지 않으면, 아무거나 하나를 뽑는다
          multiTap[0]=items[i]
          cnt+=1

# 최종적으로 플러그를 뽑는 횟수를 출력
print(cnt)
