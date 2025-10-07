'''
    다익스트라 기본문제) A->F로 가는 경로 중 가방 비용이 작게 드는 경로는? 
    가중치 그래프 vs 비가중치 그래프
    - 가중치 그래프에서는 다익스트라 알고리즘을 사용해야 한다.
    - 비가중치 그래프에서는 BFS를 통해 가장 짧은 거리를 찾을 수 있다.
'''

'''
    다익스트라: 가중치 그래프에서 시작점과 도착점이 주어졌을 때, 최단 경로를 return 하는 알고리즘이다.
    핵심 아이디어: 아직 방문하지 않은 정점 중 현재까지 알려진 거리가 가장 작은 정점들을 하나씩 확정해 나가며, 그 정점의 이웃들의 거리를 완화하는 것이다.
                방문할 수 있는 노드 중에 가장 비용이 작은 곳 방문(우선순위가 높은 곳 방문)
    구현 절차 
    1. 우선순위큐에 시작노드 추가
        2. 우선순위가 가장 높은 노드 추출
        3. 방문여부 확인
            4. 비용 업데이트
            5. 현재 노드와 연결된 노드 우선순위 큐에 추가
        6. 목적지에 기록된 비용 반환
    시간 복잡도: O(ElogV) E는 간선의 수, V는 정점의 수
'''

# 다익스트라 알고리즘 템플릿
import heapq
def dijkstra(graph, src, dst):
    costs={}
    pq=[]
    heapq.heappush(pq,(0,src))
    
    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v]=cur_cost # 1. 현재 vertex 방문 표시 
            for cost, next_v in graph[cur_v]: # 2. 연결된 vertext q에 추가
                next_cost = cur_cost+cost
                heapq.heappush(pq,(next_cost,next_v))
    return costs[dst]

graph={
    1: [(2,2),(1,4)],
    2: [(1,3),(9,5),(6,6)],
    3: [(4,6)],
    4: [(3,3),(5,7)],
    5: [(1,8)],
    6: [(3,5)],
    7: [(7,6),(9,8)],
    8: []
}

print(dijkstra(graph=graph, src=1, dst=8))
