'''
    그래프의 출발지와 목적지가 주어졌을 때, 최단 경로의 거리와 최단 경로의 모든 경로를 구하는 문제 기본 템플릿 
    -> "모든 최단경로"를 나열해야하는 문제는 BFS로 preds를 만든 뒤 백트래킹해서 경로를 추적해야한다.
    -> BFS 시 O(V+E) 만큼 걸리고, 나열 시 O(P*L) 만큼 걸림. P는 경로 수, L은 경로 길이 평균(V-1)
    -> 따라서, 총 시간복잡도는 O(V+E+P*L)
'''

from collections import deque

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


print(shortest_dist_and_paths(graph=G, src='a', dst='f'))
print(shortest_dist_and_paths(graph=H, src=0, dst=3))


'''
    최단경로 거리와 최단경로의 수를 묻는다면?
    -> 단 한번의 BFS 탐색으로 답을 구할 수 있다. 시간복잡도: O(V+E)
'''