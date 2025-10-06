'''
    택배 배달과 수거하기
'''

# 아이디어
# 규칙1. 최대한 많이 들어서 끝집부터 주고 오고 오는 길에 치운다
# -> 일단 많이 들고 가는 것부터 하자..  
# 규칙2. 올 때 많이 들고오기..
# bfs..? dfs..? 


# ------- 첫 번째 풀이 -------
# 가는 길에 다 주고, 오는 길에 다 가져오는거 반복. 다 0이 될 때까지!
def solution(cap, n, deliveries, pickups):
    answer=0
    # 집 정보: {1:(1,0), 2:(0,3), 3:(3,0), 4:(1,4), 5:(2,0)}
    house_info={}
    for i in range(n):
        house_info[i+1]=(deliveries[i], pickups[i])
    
    # key 기준으로 내림차순 정렬. 먼 곳부터 방문할 예정! 
    house_info = dict(sorted(house_info.items(), key=lambda x:x[0], reverse=True))
    
    while house_info:
        # 택배 주고 오기
        rem_delivery=cap
        add=0
        for key, (delivery, _ ) in house_info.items():
            add = max(add, key)
            if rem_delivery == 0 : break
            if delivery <= rem_delivery: 
                house_info[key]=(0,_)
                rem_delivery -= delivery
            else:
                delivery -= rem_delivery
                house_info[key]=(delivery, _)
                rem_delivery = 0
            
        # 택배 가지고 오기
        rem_pickups=cap
        for key,(_, pickup) in house_info.items():
            if rem_pickups == 0: break
            if pickup <= rem_pickups:
                house_info[key]=(_, 0)
                rem_pickups -= pickup
            else:
                pickup -= rem_pickups
                house_info[key]=(_,pickup)
                rem_pickups = 0
                
        answer += add*2
        
        
        # house_info 필터링!
        house_info = {
            k: v for k, v in house_info.items()
            if not (v[0]==0 and v[1]==0)
        }

    return answer


print(solution(cap=4, n=5, deliveries=[1, 0, 3, 1, 2], pickups=[0, 3, 0, 4, 0]))
print(solution(cap=2, n=7, deliveries=[1, 0, 2, 0, 1, 0, 2], pickups=[0, 2, 0, 1, 0, 2, 0]))

'''
    실수 회고
    1. dict를 순회하면서 크기를 바꿈 -> 파이썬 런타임 에러 => dict comprehension으로 필터링 후 dict 재생성해서 해결!
'''

# 결과: 정확성은 통과, 시간 초과!
# 왜 시간 초과일까? O(n^2)임 
# 통과 풀이 아이디어: "맨 끝 인덱스부터" 포인트 2개만 움직이는 방식이 정석...?


def solution2(cap, n, deliveries, pickups):
    answer = 0
    i = n - 1  # deliveries의 마지막 유효 인덱스
    j = n - 1  # pickups의 마지막 유효 인덱스

    # 뒤에서부터 0인 집들은 미리 당겨놓기 
    while i >= 0 and deliveries[i] == 0:
        i -= 1
    while j >= 0 and pickups[j] == 0:
        j -= 1
    
    while i >= 0 or j >= 0 :
        # 이번 트립의 최장 거리 (1-based 집번호라서 +1)
        dist = max(i,j)+1
        answer += dist*2
        
        # 배달 채우기
        carry = cap
        while i >= 0 and carry > 0 :
            if deliveries[i] <= carry:
                carry -= deliveries[i]
                deliveries[i] = 0
                i -= 1
                while i >= 0 and deliveries[i] == 0 :
                    i -= 1
            else:
                deliveries[i] -= carry
                carry = 0
        
        # 수거 채우기
        carry = cap
        while j >= 0 and carry > 0 :
            if pickups[j] <= carry:
                carry -= pickups[j]
                pickups[j] = 0
                j -= 1
                while j >= 0 and pickups[j] == 0 :
                    j -= 1
            else:
                pickups[j] -= carry
                carry = 0

    return answer


print(solution2(cap=4, n=5, deliveries=[1, 0, 3, 1, 2], pickups=[0, 3, 0, 4, 0]))
print(solution2(cap=2, n=7, deliveries=[1, 0, 2, 0, 1, 0, 2], pickups=[0, 2, 0, 1, 0, 2, 0]))