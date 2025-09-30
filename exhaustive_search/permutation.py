# 완전 탐색 기본 유형 - 순열
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