# 프로그래머스 고득점 알고리즘 dfs/bfs
# 게임 맵 최단거리
# 최단거리는 무조건 bfs로 풀어야함 -> 큐 사용

from collections import deque
def solution(maps):
    n = len(maps) # 행의 개수 
    m = len(maps[0]) # 열의 개수
    visited=[[False]*m for _ in range(n)]
    
    dirs=[(0,1),(1,0),(0,-1),(-1,0)] # 좌측부터 시계방향
    q=deque()
    q.append((0,0,1)) # 시작점
    visited[0][0] = True
    while q:
        cy,cx,d=q.popleft()
        if cy==n-1 and cx ==m-1:
            return d
        for dy,dx in dirs:
            ny,nx = cy+dy, cx+dx
            if 0<=ny<n and 0<=nx<m:
                if maps[ny][nx]==1 and not visited[ny][nx]:
                    visited[ny][nx]=True
                    q.append((ny,nx,d+1))

    return -1 

print(solution(maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))