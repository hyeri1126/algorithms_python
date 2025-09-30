# 타겟 넘버 - 프로그래머스 고득점 문제

def solution(numbers,target):
    count=0
    path=[] # ('+', 값) or ('-', 값) 기록 
    
    # 각 number 마다 +,- 값을 가질 수 있음. 
    # 그리고 이거의 합이 target이 되면 됨
    # 그니까 사실 순열,조합 그쪽 문제 아닌가?
    def dfs(index,sum):
        if index == len(numbers):
            if sum == target:
                count+=1
            return
        
        # + 선택하는 경우
        path.append(('+', numbers[index]))
        dfs(index+1, sum+numbers[index])
        path.pop()
        
        # - 선택하는 경우
        path.append(('-',sum-numbers[index])) 
        dfs(index+1, sum-numbers[index])
        path.pop()
        
    dfs(0,0)        
    return count