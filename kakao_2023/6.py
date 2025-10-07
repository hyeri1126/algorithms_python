''' 
    2023 카카오 - 미로 탈출 명령어
    n x m 격자 미로가 주어진다. (x,y) 에서 출발해 (r,c)로 이동해서 탈출해라. 
    미로 탈출 조건엔 세 가지가 있다.
        1. 격자의 바깥으로 갈 수 없다.
        2. (x,y)에서 (r,c)까지 이동하는 거리가 총 k여야 한다. (x,y)와 (r,c) 격자를 포함해 같은 격자를 두 번 이상 방문해도 된다.
        3. 미로에서 탈출한 경로를 문자열로 나타냈을 때, 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 한다.
    l = 왼쪽, r = 오른쪽, u = 위쪽, d = 아래쪽 
    input: n,m,x,y,r,c,k
'''

# 구현 아이디어
# 1. dfs로 모든 경로 전부 탐색. 어차피 종료 조건이 있으니까 괜찮음
# 2. 모든 경로 저장 -> 그 중에서 사전순으로 가장 빠른 경로 return

def solution(n, m, x, y, r, c, k):
    answer = []
    cur_str = ''
    
    def dfs(y,x,i):
        nonlocal cur_str
        if i == k:
            if y == r and x == c:
                answer.append(cur_str)
            return 
        dirs = [(0,1), (1,0), (0,-1), (-1,0)] 
        for dy, dx in dirs:
            ny,nx = y+dy, x+dx
            if 1 <= ny <= n and 1 <= nx <= m:
                if (dy,dx) == (0,1): 
                    cur_str += 'r'
                elif (dy,dx) == (1,0):
                    cur_str += 'd'
                elif (dy,dx) == (0,-1):
                    cur_str += 'l'
                elif (dy,dx) == (-1,0):
                    cur_str += 'u'
                dfs(ny,nx,i+1)
                cur_str = cur_str[:-1]
    
    dfs(x,y,0)
    
    return min(answer) if answer else "impossible"
    

# print(solution(2,2,1,1,2,2,2))
# print(solution(3,4,2,3,3,1,5))
# print(solution(3,3,1,2,3,3,4))


'''
    첫 번째 방법 
    그래프 탐색 dfs로 풀어서 풀긴 풀었는데,,, 런타임에러 발생(파이썬은 재귀가 1000을 넘으면 런타임 에러(재귀 한도) 발생 -> RecursionError)
    현재 방법은 전체 경로 열겨 DFS로 O(4^k) 걸림
    최적화 필요...
'''

'''
    그리디(greedy) 적용하기
    greedy = 지금 이 순간 가장 좋아 보이는 최적을 선택, 그 상태에서 또 같은 원칙을 반복하는 알고리즘

    사전순으로 더 빠른 글자 중 도달 가능한 것만 선택하기
    도달 가능 여부는 어떻게 알지? 현재 위치에서 도착 위치의 맨해튼 거리보다 남아있는 거리의 수가 작아야만 진행
        1. 사전순으로 이동 후보를 두기
           dirs = [(0,1), (1,0), (0,-1), (-1,0)] -> dirs = [(1,0), (0,-1), (0,1), (-1,0)]
        2. 매번 현재 위치에서 도착 위치까지의 맨해튼 거리를 구하고, 남은 이동수보다 크다면 이동
'''

# 그리디 적용하기
# dirs를 사전순으로 바꿨으니까 처음 찾는 해가 최적의 해임. 그니까 처음 해를 찾자마자 모든 dfs를 종료시키면 됨
# 모든 dfs를 종료시키는 건 True를 상위 dfs로 전파시키면서 종료시키기

def solution2(n, m, x, y, r, c, k):
    result = None 
    cur_str = []
    
    # 시작부터 불가능하면 즉시 return
    dist = abs(r-x) + abs(c-y)
    if dist > k :
        return "impossible"
    
    def dfs(y,x,i):
        nonlocal result
        if result is not None:
            return True 
        
        # 하다가 불가능하면 돌아가기
        dist = abs(r-y) + abs(c-x)
        if k-i < dist or (((k-i) - dist)%2 != 0):
            return False
        
        if i == k:
            if y == r and x == c:
                result = ''.join(cur_str)
                return True
            return False
        
        # 사전순 분기하다가 첫 해를 찾으면 즉시 종료하자! 
        dirs = [(1,0), (0,-1), (0,1), (-1,0)]
        for dy, dx in dirs:
            ny,nx = y+dy, x+dx
            if 1 <= ny <= n and 1 <= nx <= m:
                if (dy,dx) == (0,1): 
                    cur_str.append('r')
                elif (dy,dx) == (1,0):
                    cur_str.append('d')
                elif (dy,dx) == (0,-1):
                    cur_str.append('l')
                elif (dy,dx) == (-1,0):
                    cur_str.append('u')
                if dfs(ny,nx, i+1): return True
                cur_str.pop()
    
    dfs(x,y,0)
    
    
    return result if result is not None else "impossible"
    

print(solution2(2,2,1,1,2,2,2))
print(solution2(3,4,2,3,3,1,5))
print(solution2(3,3,1,2,3,3,4))


