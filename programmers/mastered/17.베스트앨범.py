"""
https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""
def solution(genres, plays):
    answer = []
    dict1={}
    dict2={}
    for i,(g,p) in enumerate(zip(genres, plays)):
        # dict1 = 장르별로 몇번째 인덱스에 몇번 플레이 되었는지.
        if g in dict1:
            dict1[g].append((i,p))
        else:
            dict1[g] = [(i,p)]
            
        # dict2 = 장르별로 얼마나 많은 play시간이 있었는지
        if g in dict2:
            dict2[g] += p
        else:
            dict2[g] = p
    
    # 가장 많이 플레이된 순으로 sorting
    # {'classic': 1450, 'pop': 3100} -> [('pop', 3100), ('classic', 1450)]
    sorted_dict2 = sorted(dict2.items(), key = lambda x:x[1], reverse = True)
    
    # sorting된 장르에서 탑2의 인덱스를 삽입
    for (genre,_) in sorted_dict2:
        top_genre = dict1[genre]
        sorted_top_genre = sorted(top_genre, key=lambda x:x[1], reverse=True)[:2]
        for j in sorted_top_genre:
            answer.append(j[0])
                
    return answer
