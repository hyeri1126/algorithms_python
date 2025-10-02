# 계단의 꼭대기를 n이라고 할 때, n개의 steps까지 올라오는 방법의 개수는 총 몇가지인가?
# 단, 한 번 올라갈 때마다 1 step 또는 2 steps 올라갈 수 있다.


# 1-1. 완전 탐색 - dfs(재귀)
# 당연히 완전 탐색 방법으로 풀 수 있다. 하지만 반복되는 부분이 많아 비효율적이다. 시간복잡도는 O(2^n) n은 steps임. 
def exhaustive_search(steps):
    cnt=0
    def dfs(sum_as_far):
        nonlocal cnt # 이 코드 없으면 에러. cnt+=1에서 cnt 값이 존재하지 않아서
        if sum_as_far == steps: 
            cnt += 1
            return
        if sum_as_far > steps:
            return
        dfs(sum_as_far + 1)
        dfs(sum_as_far + 2)
    dfs(0)
    return cnt
print(exhaustive_search(steps=5))

# 1-2. 같은 완전 탐색이지만 같은 리턴해서 합치기 
# 각 서브트리가 자기 개수를 반환하고, 즉 현재 step까지의 계단 올라오는 방법을 리턴하고 부모가 더해서 올림
# 이 방법을 추천. 메모이제이션을 붙이기 쉬움
def exhaustive_search2(steps):
    def dfs(total):
        if total == steps:
            return 1
        if total > steps:
            return 0
        return dfs(total+1)+dfs(total+2) 
    return dfs(0)

print(exhaustive_search2(steps=5))

# 2. dynamic programming - top down, 메모이제이션 활용하기
# 누적 높이 기준
def solution(steps):
    memo={}
    def dfs(total):
        if total == steps:
            return 1
        if total > steps:
            return 0
        if total not in memo:
            memo[total]=dfs(total+1)+dfs(total+2)
        return memo[total]
    return dfs(0)

print(solution(steps=5))

# 남은 계단 수
def solution2(steps):
    memo={1:1,2:2}
    def dp(n):
        if n not in memo:
            memo[n]=dp(n-1)+dp(n-2)
        return memo[n]
    return dp(steps)

print(solution2(steps=5))        
 
# 3-1. dynamic programming - bottom up, 반복문 활용
def solution3(steps):
    memo={1:1,2:2}
    for i in range(2,steps+1):
        memo[i]=memo[i-1]+memo[i-2]
    return memo[steps]

# 3-2. dynamic programming - bottom up, 공간 O(1)
def solution4(steps):
    if steps<=1:
        return 1
    a,b = 1,1
    for _ in range(2,steps+1):
        a,b=b,a+b
    return b
    
    
    
# 만약, 가능한 모든 경로를 return 하라고 한다면? -> backtracking
def climb_paths(steps):
    res, path = [], []    
    def dfs(cur_step):
        if cur_step == steps:
            res.append(path[:])
            return
        if cur_step > steps:
            return
        path.append(1)
        dfs(cur_step+1)
        path.pop()
        path.append(2)
        dfs(cur_step+2)
        path.pop()
    dfs(0)
    return res

print(climb_paths(steps=3))            