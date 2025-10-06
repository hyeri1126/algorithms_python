# 타겟 넘버 - 프로그래머스 고득점 문제

def solution(numbers, target):
    count = 0
    path=[]
    def dfs(idx):
        nonlocal count
        if idx == len(numbers): # 재귀 종료 조건: numbers를 전체 다 썼다면!
            if sum(path) == target:
                count += 1
            return
        path.append(numbers[idx])
        dfs(idx+1)
        path.pop()
        
        path.append(-numbers[idx])
        dfs(idx+1)
        path.pop()
    dfs(0)
    return count

print(solution(numbers=[1, 1, 1, 1, 1], target=3))
print(solution(numbers=[4, 1, 2, 1], target=4))