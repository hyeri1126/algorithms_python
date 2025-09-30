# 완전 탐색의 기본 구현 - 부분집합
# nums=[1,2,3,4]로 만들 수 있는 부분집합을 모두 반환하시오
# 조합을 반복하면 된다. 

# 조합 기반 백트래킹
def solution(nums):
    result=[]
    
    def combitation(nums,k):
        ans = []
        def backtrack(start, curr):
            if len(curr) == k :
                ans.append(curr[:]) 
                return
            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
        backtrack(0, [])
        return ans
    
    for i in range(len(nums)+1):
        result.append(combitation(nums,i))
        
    return result

print(solution([1,2,3,4])) #ouput: [[[]],[[1],[2],[3],[4]],[[1,2],[1,2]..],.. ] 


    
def subset2(nums):
    ans = []
    def backtrack(start, curr):
        if len(curr) == k :
            ans.append(curr[:]) 
            return
        for i in range(start,len(nums)):
            curr.append(nums[i])
            backtrack(i+1,curr)
            curr.pop()
    for k in range(len(nums)+1):
        backtrack(0, [])
  
    return ans

print(subset2([1,2,3,4])) #ouput: [[],[1],[2],[3],[4],[1,2] ..]





# dfs로 푸는 방법
def solution3(nums):
    result=[]
    def dfs(idx, path):
        if idx == len(nums):
            result.append(path[:])
            return
        dfs(idx+1, path) # 1) 현재 원소 선택하지 않음
        dfs(idx+1, path+[nums[idx]]) # 2) 현재 원소 선택함
        
    dfs(0,[])   
    return result
   
print(solution3(nums=[1,2,3]))