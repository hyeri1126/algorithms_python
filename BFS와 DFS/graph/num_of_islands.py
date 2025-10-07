# Number of Islands
# "1"(land)과 "0"(water)으로 이루어진 지도를 표현하는 m x n 이차원 배열이 주어질 때, 이 지도에 표시된 섬들의 총 갯수를 반환하시오
# Ex) input: grid=[['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']], output: 1

# 1. bfs 
from collections import deque

def solution(grid):
    num_of_islands=0
    m,n = len(grid), len(grid[0])
    visited=[[False]*n for _ in range(m)]
    
    def bfs(y,x):
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        q = deque()
        q.append((y,x))
        while q :
            cy,cx = q.popleft()
            for dy,dx in dirs:
                ny,nx = cy+dy, cx+dx
                if 0<=ny<m and 0<=nx<n :
                    if grid[ny][nx] == '1' and visited[ny][nx] == False:
                        q.append((ny,nx))
                        visited[ny][nx] = True
    for y in range(m):
        for x in range(n):
            if grid[y][x] == '1' and not visited[y][x]:
                num_of_islands += 1
                bfs(y,x)
    return num_of_islands

print(solution([['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]))


# 2. dfs