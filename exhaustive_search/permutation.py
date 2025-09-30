# 완전 탐색 기본 유형 - 순열

# 1. 백트래킹
def permute(nums):
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    ans=[]
    backtrack([])
    return ans

print(permute([1,2,3,4]))


# 2. dfs 
def solution2(nums):
    result=[]
    visitied=[False]*len(nums)
    def dfs(path):
        if len(path)==len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if not visitied[i]:
                visitied[i]=True
                dfs(path+[nums[i]])
                visitied[i]=False
    dfs([])
    return result 

print(solution2(nums=[1,2,3])) #output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] -> 이진트리 리프노드 왼쪽부터의 순서와 같음


# 순열은 백트래킹이든, dfs 방법이든 순서 고려해야함. 방문 여부가 필요함. 
