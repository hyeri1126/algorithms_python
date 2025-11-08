from collections import defaultdict
import heapq

def solution(tickets):
    # 각 출발지 -> 도착지들을 사전순으로 꺼내기 위해 min-heap으로 관리
    graph = defaultdict(list)
    for a, b in tickets:
        heapq.heappush(graph[a], b)

    route = []          # 완성 경로(역순으로 쌓았다가 뒤집지 않고 appendleft 느낌으로 처리)
    stack = ["ICN"]     # 항상 ICN에서 출발

    # Hierholzer's algorithm (iterative)
    while stack:
        cur = stack[-1]
        if graph[cur]:
            # 해당 노드에서 갈 수 있는 곳 중 사전순으로 가장 앞선 공항부터 소모
            nxt = heapq.heappop(graph[cur])
            stack.append(nxt)
        else:
            # 막다른 곳이면 경로에 기록하고 한 단계 되돌아감
            route.append(stack.pop())

    # route는 거꾸로 쌓였으므로 뒤집은 결과가 정답
    return route[::-1]