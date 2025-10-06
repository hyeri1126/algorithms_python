'''
    프로그래머스 고득졈 알고리즘 - 네트워크
    네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미한다. 
    ** 제약사항 **
        i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][i] == 1
        computer[i][i]는 항상 1이다
'''


# 아이디어
# 인접 행렬 -> 인접 리스트로 바꾸기
# 모든 vertex에 대해 dfs 탐색!
def solution(n, computers):
    def mat_to_list(mat):
        n = len(mat)
        adj = {i:[] for i in range(n)}
        
        for i in range(n):
            for j in range(n):
                if mat[i][j] and i != j:
                    adj[i].append(j)
        
        return adj
    def dfs(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs(v)

    adj = mat_to_list(computers)
    cnt = 0
    visited= set()
    for u in range(n):
        if u not in visited:
            cnt += 1
            dfs(u)
    return cnt
                    
        

print(solution(n=3, computers=[[1,1,0],[1,1,0],[0,0,1]]))


# 인접 행렬 그대로 두고 풀어보기
def solution2(n, computers):
    visited= [False]*n
    
    def dfs(u):
        visited[u] = True
        for v in range(n):
            if computers[u][v] and not visited[v] and u != v:
                dfs(v)
    cnt = 0 
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i)
    return cnt
            
print(solution2(n=3, computers=[[1,1,0],[1,1,0],[0,0,1]]))

