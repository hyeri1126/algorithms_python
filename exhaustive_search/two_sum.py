# 완전 탐색 기본 유형 - two sum
# [4,9,7,5,1]에서 두 개의 숫자를 더해서 12가 될 수 있나요? (중복x) -> 중복 x면 조합으로!

# 1. 재귀
def solution(nums,k,target):
    ans=[]
    def backtrack(start, curr):
        if len(curr) == k :
            if sum(curr) == target:
                ans.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
    backtrack(0,[])
    return ans

print(solution([4,9,7,5,1],3,15))


# 2. 반복문 -> 두 개의 숫자니까 반복문 2번 쓰면 됨
def solution2(nums, target):
    ans=[]
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                ans.append([nums[i],nums[j]])
    return ans
        
print(solution2([1,2,3,4],5))


# 결론: 배열에서 k개의 원소를 뽑아 합이 target이 되는 경우 찾기 유형은 k에 따라 이중/삼중/사중 for문을
# 일일이 작성해야함. 따라서 재귀 구조를 사용하기! 재귀는 일반화 가능