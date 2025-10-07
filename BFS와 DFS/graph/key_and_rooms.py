# 0번방부터 n-1번방까지 총 n개의 방이 있다. 0번 방을 제외한 모든 방은 잠겨있다. 각 방에 방문할 때, 열쇠뭉치를 찾을 수 있고
# 열쇠의 해당 번호에 해당하는 방을 잠금 해제할 수 있다. 모든 방을 방문할 수 있다면 True, 그렇지 않다면 False를 반환하시오
# input: rooms =[[1],[2],[3],[]], output: True

from collections import deque

# 1. 큐에 key를 담았음. 방문할 예정임을 나타냄 
def solution(rooms):
    n = len(rooms)
    visited = [False]*(n) # 방 방문 여부
    # bfs? dfs? 
    # 일단 bfs로 해보기 
    q = deque()
    # q.append(rooms[0]) # q = [[1,2]] -> 하나씩 추가해애함 q = [1,2] 이렇게 되어야함
    visited[0] = True # 0번 방 들어감 -> 방문 처리
    # 0번 방에서 얻은 키를 큐에 추가
    for key in rooms[0]:
        q.append(key)
  
    # key들을 획득하면 q에 넣기. 나중에 방문할 예정을 나타냄
    while q:
        # key를 통해 열 수 있는 문으로 이동
        cur_key = q.popleft()
        if not visited[cur_key]: # 방문하지 않았던 방만 키를 통해 방문
            visited[cur_key] = True
            for key in rooms[cur_key]: # 거기에 있는 키 다시 큐에 담기 
                if not visited[key]: # 만약 이미 방문했다면 큐에 키를 추가할 필요 없음 -> 중복 방지!! 
                      q.append(key)
                      
    # visited가 전부 True면 True, 그렇지 않으면 False
    # for visit in visited:
    #     if visit == False:
    #         return False
    # return True
    return all(visited)

print(solution(rooms=[[1],[2],[3],[]]))
print(solution(rooms=[[1,3],[3,0,1],[2],[0]]))
     

    
# 2. 큐에 방을 넣는 방법 - 
