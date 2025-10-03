'''
    Unique Paths
    이 로봇은 m x n grid 위에 있다. 로봇은 한 번에 오른쪽이나 아래쪽으로만 움직일 수 있다.
    처음에 grid[0][0]에 위치해있고 grid[m-1][n-1]로 이동할 때, 도달할 수 있는 가능한 unique paths의 수를 반환하라.
    input: m=3, n=7, output: 28
    테스트 케이스는 답이 2*(10^9) 이하가 되도록 생성한다.
'''

# 1-1. 완전탐색(dfs)
# m=3, n=7 일 때, 오른쪽으로 6번 가고 아래쪽으로 2번 가는 조합으로 unique path를 만들 수 있다.
# 조합이다! 즉, 8C2=8C6 -> 시간복잡도 계산하기 위해 알아야함
# 시간복잡도는? O(m+n-2Cm-1) -> 매우매우 큼!!!! -> 최적화 필요

def solution(m,n):
    def dfs(y,x):
        if y == 0 and x == 0 : return 1
        if y < 0 or x < 0 : return 0
        return dfs(y-1,x) + dfs(y,x-1)
    return dfs(m-1,n-1) # 로봇이 grid[m-1][n-1]에 도착했을 때 unique paths의 수를 반환

print(solution(m=3,n=7))


# 1-2. 완전탐색(dfs) - 기준을 시작으로 잡으면?
def solution3(m,n):
    def dfs(y,x):
        if y == m-1 and x == n-1:
            return 1
        if y>m-1 or x>n-1:
            return 0
        return dfs(y+1,x) + dfs(y,x+1)
    return dfs(0,0)
print(solution3(m=3,n=7))

# 2-1. 완전탐색에 메모이제이션 적용 -> dp(top-down)
# 시간복잡도는? O(m*n), 최대 10^4 따라서 시간 초과 x
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

# 2-2. 위 코드 Bottom-up으로 바꿔보기, dp table을 채워나가는 방식! tabulation이라고도 한다.
def solution4(m,n):
    dp=[[0]*n for _ in range(m)]
    for i in range(m):
        dp[i][0]=1
    for j in range(n):
        dp[0][j]=1
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
       

    