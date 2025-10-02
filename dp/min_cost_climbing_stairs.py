# min cost climbig stairs
# 계단을 한 번 올라갈 때마다 1 step 또는 2 steps 올라갈 수 있다. 정수형 배열 cost가 주어지는데
# cost[i]는 i번 째 계단을 밟았을 때 지불해야 하는 비용이다. 
# 처음 시작은 index 0 또는 index 1 중 한 곳에서 시작할 수 있다. 
# 계단의 꼭대기에 도착하기 위해 지불해야하는 비용의 최소값을 반환하라.
# input: cost=[10,15,20], output: 15 -> # 15
# input: cost=[1,100,1,1,1,100,1,1,100,1], output:6

# 꼭대기에 가는 방법은 여러개가 존재. 근데 각 계단마다 cost가 존재.
# 최소 비용은?
# 완전 탐색 먼저. 모든 경우의 수에 대한 cost 값을 같이 구하기

# 1. 계단을 올라가는 모든 경우의 수 구하기
#    -> 각 칸마다 올라오는 방법의 수를 return 하는 방법으로 
# 2. 경우의 수에 대한 cost 비용을 따로 저장하기 -> costs={}
# 3. costs에서 최소값을 return 하기

# 각 층까지 도달하는 cost의 최소값을 반환하도록 구성. 현재 층까지 오는 방법은 오직 2개뿐. 바로 아래에서 올라오거나 두칸 아래에서 올라오거나 그 중 최소 비용을 return 하기만 하면 됨.
def min_cost_climb(cost):
    cost = cost + [0]
    steps=len(cost)
    def dfs(rem_step): 
        if rem_step == 0 : return 0
        if rem_step == 1 : return cost[0] 
        if rem_step < 0 : return 0
        left = dfs(rem_step-1)
        right = dfs(rem_step-2)
        return min(left, right) + cost[rem_step-1]
    return dfs(steps)
print(min_cost_climb(cost=[10,15,20]))

# 위 방법 최적화 -> 메모이제이션 적용하기
def min_cost_climb_dp(cost):
    cost = cost + [0]
    steps=len(cost)
    memo={}
    def dfs(rem_step):
        if rem_step == 0 : return 0
        if rem_step == 1 : return cost[0] 
        if rem_step not in memo :
            left = dfs(rem_step-1)
            right = dfs(rem_step-2)
            memo[rem_step]=min(left, right) + cost[rem_step-1]
        return memo[rem_step]
    return dfs(steps)
print(min_cost_climb_dp(cost=[10,15,20]))

def dp_topdown(cost):
    memo={}
    def dp(n):
        if n == 0 or n == 1:
            return 0
        if n not in memo:
            memo[n]=min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2])
        return memo[n]
    return dp(len(cost))

print(dp_topdown(cost=[10,15,20,17,1]))

# 위 방식은 top-down 방식임. bottom-up으로 바꾸기
def dp_bottomup(cost):
    memo={0:0, 1:0}
    def dp(n):
        for i in range(2, n+1):
            memo[i]=min(memo[i-1]+cost[i-1], memo[i-2]+cost[i-2])
        return memo[n]
    return dp(len(cost))
print(dp_bottomup(cost=[10,15,20,17,1]))

    


# ------ 가장 처음에 생각했던 완전탐색 방법(비효율적) ----------
def solution(cost):
    result,path=[], []
    steps=len(cost)+1
    def dfs(cur_step):
        if cur_step == steps: 
            result.append(sum(path))
            return 
        if cur_step > steps:
            return 
        path.append(cost[cur_step] if 0 <= cur_step < steps-1 else 0)
        dfs(cur_step+1)
        path.pop()
        path.append(cost[cur_step+1] if 0 <= cur_step+1 < steps-1 else 0)
        dfs(cur_step+2)
        path.pop()
    dfs(0)
    return min(result)
print(solution(cost=[10,15,20]))