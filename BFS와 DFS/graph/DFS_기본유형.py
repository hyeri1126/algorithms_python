'''
    1. G(V,E)가 인접 리스트로 주어졌을 때 그래프 전체 순회 - 재귀
    2. G(V,E)가 인접 리스트로 주어졌을 때 그래프 전체 순회 - 반복
'''
G = {
    1: [2,3],
    2: [1,4],
    3: [1,4],
    4: [2,3]
}

# 1. 그래프 순회 - 재귀
def solution(graph):
    visited = set()
    order=[]
    def dfs(u):
        visited.add(u)
        order.append(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
    for u in graph:
        if u not in visited:
            dfs(u)
    return order

print(solution(graph=G))
        