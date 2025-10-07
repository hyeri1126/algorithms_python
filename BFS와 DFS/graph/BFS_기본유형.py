'''
    BFS를 적용할 수 있는 기본 유형
    1. 최단 거리: BFS 레벨이 곧 거리 -> dist[v]
    2. 최단 경로의 개수 -> BFS 중 ways[v] 누적(동일 거리로 들어올 때 더함)
    3. 최단 경로(path) -> BFS로 만든 최단경로 DAG(preds) 위에서 DFS 백트래킹으로 나열
'''

# 인접 리스트 - undirected, 무가중치
G = {
    'a': ['b'],
    'b': ['a', 'c', 'e'],
    'c': ['b', 'd'],
    'd': ['c', 'e', 'f'],
    'e': ['b', 'd', 'f'],
    'f': ['d', 'e'],
}
H = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2],
}

from collections import deque

# 1. 최단 거리 - input: graph=인접리스트, src: 출발지, dst: 도착지 output: 최단 거리: int
def shortest_path(graph, src, dst):
    dist={src:0}
    q=deque([src])
    while q:
        cur_v = q.popleft()
        if cur_v == dst: return dist[cur_v]
        for v in graph[cur_v]:
            if v not in dist:
                dist[v]=dist[cur_v]+1
                q.append(v)
    return None

# 테스트
print(shortest_path(graph=H, src=0, dst=3))


# 2. 최단 경로의 수 - input: graph, src, dst ouput: int(최단 거리의 수)
def count_shortest_paths(graph, src, dst):
    dist={src:0}
    ways={src:1}
    q=deque([src])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v]=dist[u]+1
                ways[v]=ways[u]
                q.append(v)
            elif dist[v] == dist[u]+1: # 동일거리로 들어왔다면? 경로 추가!
                ways[v] += ways[u]
    return ways.get(dst)

# 테스트
print(count_shortest_paths(graph=H, src=0, dst=3))


# 3. 하나의 최단 경로(path)
def one_shortest_path(graph, src, dst):
    dist={src:0}
    parent={src:None}
    q=deque([src])
    while q:
        u=q.popleft()
        if u == dst: break
        for v in graph[u]:
            if v not in dist:
                dist[v]=dist[u]+1
                parent[v]=u
                q.append(v)
                
    # 백트래킹해서 경로 찾기
    path,cur=[],dst
    while cur is not None:
        path.append(cur)
        cur=parent[cur]
        
    return path[::-1]

print(one_shortest_path(graph=H, src=0, dst=3))

# 4. 모든 최단 경로(paths)
def all_shortest_paths(graph, src, dst):
    # 1) BFS로 최단거리 dist와 전임자 목록 preds 만들기
    dist={src:0}
    preds={src:[]}
    q=deque([src])
    while q:
        u=q.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v]=dist[u]+1
                preds[v]=[u]
                q.append(v)
            elif dist[v] == dist[u]+1: # v로 가는 또 다른 최단 부모가 있다면 추가!
                preds[v].append(u)
    
    if dst not in dist: return None # dst로 도달 불가
    
    # 2) preds를 이용해서 dst->src 역추적(DFS 백트래킹)으로 모든 최단경로 나열
    paths=[]   
    def backtrack(cur, path_rev):
        if cur == src:
            paths.append(list(reversed(path_rev)))
            return
        for p in preds[cur]:
            path_rev.append(p)
            backtrack(p, path_rev)
            path_rev.pop()
    backtrack(cur=dst, path_rev=[dst])
    return paths

print(all_shortest_paths(graph=H, src=0, dst=3))


# -------- 기본 유형 복합 문제 --------

'''
    그래프의 출발지와 목적지가 주어졌을 때, 최단 경로의 거리와 최단 경로의 모든 경로를 구하는 문제 기본 템플릿 
    -> "모든 최단경로"를 나열해야하는 문제는 BFS로 preds를 만든 뒤 백트래킹해서 경로를 추적해야한다.
    -> BFS 시 O(V+E) 만큼 걸리고, 나열 시 O(P*L) 만큼 걸림. P는 경로 수, L은 경로 길이 평균(V-1)
    -> 따라서, 총 시간복잡도는 O(V+E+P*L)
'''

def shortest_dist_and_paths(graph, src, dst):
    # src/dst 유효성 체크
    if src not in graph or dst not in graph: return False
    
    # 1) BFS: dist와 최단경로 전임자 목록(preds) 만들기
    dist={src:0}
    preds={src:[]} # 각 정점의 최단경로 상 부모들
    q=deque([src])
    
    while q:
        u = q.popleft()
        for v in graph.get(u):
            if v not in dist:
                dist[v]=dist[u]+1
                preds[v]=u
                q.append(v)
            elif dist[v]==dist[u]+1:
                preds[v].append(u)
        
    # 경로 찾기 - 백트래킹으로 모든 최단 경로 복원 (dst->src 역추적)
    paths=[]
    def dfs(c_node, path_rev):
        if c_node == src:
            paths.append(list(reversed(path_rev)))
            return
        for v in preds.get(c_node):
            path_rev.append(v)
            dfs(v,path_rev)
            path_rev.pop()
    
    dfs(dst, [dst])
    return dist[v], paths




print(shortest_dist_and_paths(graph=G, src='a', dst='f'))
print(shortest_dist_and_paths(graph=H, src=0, dst=3))


'''
    최단경로 거리와 최단경로의 수를 묻는다면?
    -> 단 한번의 BFS 탐색으로 답을 구할 수 있다. 시간복잡도: O(V+E)
'''