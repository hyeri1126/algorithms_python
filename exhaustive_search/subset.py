# 완전 탐색의 기본 구현 - 부분집합
# nums=[1,2,3,4]로 만들 수 있는 부분집합을 모두 반환하시오
# 조합을 반복하면 된다. 

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