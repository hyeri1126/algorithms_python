# 그래프가 주어졌을 때, 그래프 순회 bfs 기본 방법
from collections import deque

graph = {
    'A':['B','D','E'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['A','B'],
    'E':['A']
}

def bfs(graph, start_v):
    visited=[start_v]
    q = deque()
    q.append(start_v)
    while q:
        cur_v = q.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                q.append(v)
                visited.append(v)
    return visited


print(bfs(graph,'A'))
