# Shortes Path in Binary Matrix
# n x n binary matrix인 grid가 주어졌을 때, 출발지에서 목적지까지 도착하는 가장 빠른 경로의 길이를 반환하시오, 만약 경로가 없다면 -1 반환
# 출발지: top-left cell, 목적지: bottom-right cell
# 값이 0인 cell만 지나갈 수 있으며, cell끼리는 8가지 방향으로 연결되어 있다. (edge와 corner 방향)

from collections import deque

def solution(grid):
    n = len(grid)
    # 시작/도착이 막혀 있으면 불가
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    # n == 1 특수 케이스
    if n == 1:
        return 1
    visited=[[False]*n for _ in range(n)]
    def find_shortest_path(start, destination):
        path=0
        dirs=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        q = deque()
        q.append((0,0,1))
        visited[start[0]][start[1]] = True
        while q:
            cy,cx, d = q.popleft()
            if cy == destination[0] and cx == destination[1]:
                return d
            for dy,dx in dirs:
                ny,nx = cy+dy, cx+dx
                if 0<=ny<n and 0<=nx<n:
                    if grid[ny][nx] == 0 and not visited[ny][nx]:
                        q.append((ny,nx, d+1))
                        visited[ny][nx] = True
        return -1

    shortest_path = find_shortest_path((0,0),(n-1,n-1))                
                
    return shortest_path

print(solution([[0,0,0],[1,1,0],[1,1,0]]))
print(solution([[1,0,0],[1,1,0],[1,1,0]]))

# path를 따로 정의하는 것이 아니라 각 좌표별로 좌표까지의 거리를 같이 저장해야한다. 
# + 항상 dfs 함수를 따로 작성하던 습관 떄문에 find_shortest_path 함수를 정의하긴 했지만 사실 따로 정의할 필요 없이 solution 내에서 한번에 처리할 수 있었다. 


def solution2(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    if n == 1:
        return 1
    visited = [[False]*n for _ in range(n)]
    dirs=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    q = deque([(0,0,1)])
    visited[0][0] = True
    while q:
        cy,cx,c_len = q.popleft()
        if cy == n-1 and cx == n-1 :
            return c_len
        for dy,dx in dirs:
            ny,nx = cy+dy, cx+dx
            if 0<=ny<n and 0<=nx<n:
                if grid[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((ny,nx,c_len+1))
                    visited[ny][nx] = True
    return -1

print(solution2(grid=[[0,0,0],[1,1,0],[1,1,0]]))
print(solution2(grid=[[1,0,0],[1,1,0],[1,1,0]]))
