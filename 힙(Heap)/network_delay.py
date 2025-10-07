'''
    Network Delay Time
    n개의 노드로 구성된 네트워크가 있으며, times[i]=[ui,vi,wi] 리스트가 주어진다. 이 때 ui 노드에서 신호를 보내서
    vi 노드에 도달하는데 걸리는 시간을 wi라고 한다. 
    k 노드에서 신호를 보낼 때, 모든 노드에 신호가 도달하기 위한 최소 비용을 반환하시오. 하나의 노드라도 도달하지 못한다면 -1을 반환
    ** 제약조건 ** 
        1 <= k <= n <= 100 -> 시간복잡도 O(n^3)까지 가능
        1 <= times.length <= 6000 -> 그래프 구현에 시간이 걸림. edge->adj 변환하는 함수 시간 복잡도: O(n) -> 시간 통과 
                                  -> 다익스트라 알고리즘: O(ElogE) times.length는 그래프의 간선의 수를 나타냄. -> 시간 통과 
        times[i].length == 3
        1 <= ui, vi <= n
        ui != vi
        1 <= wi <= 100 -> 시간복잡도와 관련 없음
        모든 (ui, vi) 쌍은 unique 합니다.
    input: times=[[2,1,2],[2,3,5],[2,4,1],[4,3,3]],n=4,k=2  ouput: 4
    input: times=[[2,1,2],[2,3,5],[2,4,1],[4,3,3]],n=4,k=3  ouput: -1
'''
from collections import defaultdict
import heapq

def solutioin(times,n,k):
    # 간선 리스트 -> 인접 리스트
    def edges_to_adj(edges):
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
        return adj
    def dijkstra(graph, src, n):
        costs={}            
        pq=[]
        heapq.heappush(pq, (src,0))
        while pq:
            cur_v, cur_cost = heapq.heappop(pq)
            if len(costs) == n : return cur_cost 
            if cur_v not in costs:
                costs[cur_v]=cur_cost
                for next_v, cost in graph[cur_v]:
                    next_cost = cost+cur_cost
                    heapq.heappush(pq,(next_v,next_cost))
        return -1
    graph = edges_to_adj(edges=times)
    return  dijkstra(graph,k,n)   

print(solutioin(times=[[2,1,2],[2,3,5],[2,4,1],[4,3,3]], n=4, k=2))
print(solutioin(times=[[2,1,2],[2,3,5],[2,4,1],[4,3,3]], n=4, k=3))