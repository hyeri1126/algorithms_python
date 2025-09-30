# 완전 탐색의 기본 구현 - 조합

# 1. 백트래킹
def combination(nums,k):
    ans=[]
    def backtrack(start,curr):
        if len(curr) == k:
            ans.append(curr[:])
            return
        for i in range(start,len(nums)):
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
    backtrack(0,[])
    return ans

print(combination(nums=[1,2,3,4],k=2))

# 2. dfs
def solution2(nums,k):
    result=[]
    def dfs(start, path):
        if len(path) == k :
            result.append(path[:])
            return
        for i in range(start, len(nums)):
            dfs(i+1, path+[nums[i]])
    dfs(0, [])
    return result