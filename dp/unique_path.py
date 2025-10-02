'''
    Unique Paths
    이 로봇은 m x n grid 위에 있다. 로봇은 한 번에 오른쪽이나 아래쪽으로만 움직일 수 있다.
    처음에 grid[0][0]에 위치해있고 grid[m-1][n-1]로 이동할 때, 도달할 수 있는 가능한 unique paths의 수를 반환하라.
    input: m=3, n=7, output: 28
'''

# 1. 완전탐색(dfs), 시간복잡도: O(2^n) n은 y x x 
def solution(m,n):
    def dfs(y,x):
        if y == 0 and x == 0 : return 1
        if y < 0 or x < 0 : return 0
        return dfs(y-1,x) + dfs(y,x-1)
    return dfs(m-1,n-1) # 로봇이 grid[m-1][n-1]에 도착했을 때 unique paths의 수를 반환

print(solution(m=3,n=7))

# 2. 완전탐색에 메모이제이션 적용 -> dp(bottom-up)
def solution2(m,n):
    memo={}
    def dp(y,x):
        if y == 0 and x == 0 : return 1
        if y < 0 or x < 0 : return 0
        if (y,x) not in memo:
            memo[(y,x)] = dp(y-1,x) + dp(y,x-1)
        return memo[(y,x)]
    return dp(m-1,n-1)

print(solution2(m=3, n=2))