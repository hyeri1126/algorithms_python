'''
    이모티콘 할인행사
    ** 제약 조건 **
        1 ≤ emoticons의 길이 = M ≤ 7 
            - 이모티콘이 M개라면, 각 이모티콘에 가능한 할인율(4가지) 중 하나를 배정 => 경우의 수 4^M
            - M <= 7 이여서 충분히 브루트포스 가능!        
'''

# 목표: 이모티콘 플러스 가입을 최대한 많이! 
# -> 최소한의 할인으로 구매 가격을 넘기게 만드는 경우가 많아야함! 
# 1. 최소한의 할인율 먼저 구하기 

def solution(users, emoticons):
    rates=[10,20,30,40] # 가능한 할인율
    
    # 1. 할인율 중 최소값 구하기 
    min_rate=1000
    for user in users:
        min_rate=min(min_rate, user[0])

    # 2. 최소값보다 작은 할인율 제거. 적용 가능한 할인율만 남겨두기
    rates=[r for r in rates if r >= min_rate]
    
    m = len(emoticons) 
    pick = [0]*m # 각 이모티콘에 배정된 할인율
    best_sub, best_rev = -1, -1

    def evaluate(): # 이모티콘 할인율이 정해졌을 때, 그때 모든 고객에게 적용했을 경우 가입자 수와 매출액!
        subscribers=0 # 이모티콘 가입자 수
        revenue=0 # 매출액
        for user in users:
            total=0
            min_disc, threshold = user
            for i in range(m): # 이모티콘 개수만큼 반복
                if pick[i] >= min_disc:
                    total += emoticons[i]*((100-pick[i])*0.01)
            if total >= threshold:
                # 이모티콘 가입!
                subscribers += 1
            else:
                revenue += total
        return [subscribers, revenue]
        
                
        
    # 모든 아이템에 남은 할인율 다 적용해보면 됨! 그니까 
    # 만약 지금처럼 rates가 2개 남으면 아이템 당 선택지는 2개니까 이진트리가 만들어질거임
    # 근데 rates에 남은게 3개라면 삼진트리, 4개라면 사진트리가 된다는건가? 
    # 이진트리면 dfs 내부에서 2번 재귀하면 될 것이고 3번이면 3번 재귀고 4번이면 4번 재귀하면 되는 것 같기도 함?/
    def dfs(i):
        nonlocal best_sub, best_rev
        if i == m: # base 조건은 dfs를 4번 즉, 아이템 수 만큼 호출했다면 종료!
            subscribers, revenue = evaluate()
            # subscribers은 클수록 좋음! 같다면 revenue이 클수록 좋음!
            if best_sub > subscribers:
                return
            if best_sub < subscribers: # 구독자 수 많기만 하면 무조건 바꾸고 
                best_sub = subscribers
                best_rev = revenue
                return
            if best_sub == subscribers: # 같으면 revenue이 더 커야 바꾸기!
                if best_rev <= revenue:
                    best_sub = subscribers
                    best_rev = revenue
            return
        # 남은 할인율 선택지만큼 Dfs를 호출해야하는데? .. 항상 바뀌는데 어떻게 dfs를 작성해놓지?
        # 이 방법이 아닌가.. 일단 2개라고 가정해보자! (len(emoticons)==2 라고 가정!)
        for r in rates:
            pick[i] = r
            dfs(i+1)
            
    dfs(0)
    return [best_sub, int(best_rev)]


print(solution(users=[[40, 10000], [25, 10000]], emoticons=[7000, 9000]))
print(solution(users=[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], emoticons=[1300, 1500, 1600, 4900]))



'''
    회고 
    막혔던 부분
        처음에 dfs를 활용해야하는 것 까진 잘 생각했다! dfs(0)부터 시작해서 dfs(i)의 i가 이모티콘의 길이가 되면 dfs를 종료시키는 조건까진 잘 생각했다
        그런데, 왜 그 후 계산하는게 막혔을까? pick을 생각하지 못했다. pick은 각 이모티콘의 할인율을 저장하는 배열,, 이걸 생각하지 못했던 부분이 큰 것 같고..
        "조합 선택"과 "결과 계산"을 한 함수에서 생각하니,, ㅠㅠ 탐색과 시뮬레이션(evaluate)을 분리해서 생각하기!
        또,, dfs() 에서 재귀로 dfs를 두 번 호출하는 건 많이 해봤다. 이진트리 구조! 근데 dfs 안에서 dfs를 여러번 호출하는 건 처음 해봐서?
        여러번 호출해야겠다는 건 분명 생각했는데,, 막상 구현이 어려웠다,, 하지만 실제로 해보니 별 거 없었다는 걸 알았다. 
'''