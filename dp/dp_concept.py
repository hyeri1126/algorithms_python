# dynamic programming
# 개념: 문제에 대한 정답이 될 가능성이 있는 모든 해결책을 "체계적"이고 "효율적"으로 탐색하는 방법
# DP 접근 방법
# 1. DP는 크고 복잡한 문제를 subproblem으로 나눈다.  
# 2. 하위문제의 답을 계산한다.
# 3. 하위 문제의 답을 통해 원래 문제의 답을 계산한다
# 하위 문제의 답을 계산하다 보면 중복 하위 문제(overlapping subpromblems)가 나타난다. 따라서 메모이제이션을 통해 재계산을 하지 않도록 한다.
# DP를 푸는 방식은 두가지가 존재
# 1. Top-down: 재귀를 통해 구현, 메모이제이션이라고 한다. 재귀를 통해 위에서부터 아래로 뻗어나가지만 사실상 답을 구하기 위에서는 아래에서부터 위로 합쳐져간다. 
# 2. Bottom-up: 반복문을 통해 구현, dp 테이블을 활용한다.

# DP의 대표문제: 피보나치 수열
# 피보나치 수열은 중복 하위 문제가 많다. 이를 메모이제이션 없이 전부 계산한다면 시간복잡도는 O(2^n)이다. 
# 이를, 메모이제이션해서 풀면 시간 복잡도는 O(n)이 된다. 

# 피보나치 - Top-down

# 잘못된 예시 - 답은 구해지지만 메모이제이션이 전혀 안됨, 완전탐색이나 마찬가지(최적화x)
# why? fibo_topdown 매 호출마다 새 memo dict 생성
# def fibo_topdown(n):
#     memo={}
#     if n == 1 or n == 2 :
#         return 1
#     if n not in memo:
#         memo[n]=fibo_topdown(n-1)+fibo_topdown(n-2)
#     return memo[n]

# 올바른 정답 -> 항상 메모리는 재귀 전체에 공유되어야한다. 따라서 클로저로 공유하기 혹은 인자로 전달해도 됨
def solution(n):
    memo={1:1, 2:1}
    def dp(k):
        if k not in memo:
            memo[k]=dp(k-1)+dp(k-2)
        return memo[k]
    return dp(n)
    
print(solution(n=3))

# 피보나치 - Bottom-up
def fibo_bottomup(n):
    memo={1:1, 2:1}
    for i in range(3,n+1):
        memo[i]=memo[i-1]+memo[i-2]
    return memo[n]

print(fibo_bottomup(n=3))

# 피보나치 - bottom-up 최적화 
def fibo_bottomup_optim(n):
    # memo dictionary 사용 x -> 공간 복잡도 낮아짐
    if n <= 0: return 0
    if n == 1: return 1
    a,b = 0,1  # F(0), F(1)
    for _ in range(2, n+1):
        a,b = b, a+b
    return b
    