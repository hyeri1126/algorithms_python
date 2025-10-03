'''
    Longest Consecutive Sequence
    정렬되어 있지 않은 정수형 배열 nums가 주어졌다. nums 원소를 가지고 만들 수 있는 가장 긴 연속된 수의 갯수는 몇개인지 반환하시오.
    ** 제약조건 **
        0 <= nums.length <= 10^5 -> 시간복잡도는 O(n^2) 보다 작아야한다. 
        -10^9 <= nums[i] <= 10^9
    input: nums=[100,4,200,1,3,2] ouput: 4
    input: nums=[0,3,7,2,5,8,4,6,0,1] ouput: 9
''' 

# 처음 풀이 : 시간복잡도 O(nlogn)
def solution(nums):
    nums.sort() #[1,2,3,4,100,200], [0,0,1,2,3,4,5,6,7,8]
    count = 1
    answer=set()
    for idx, num in enumerate(nums[1:], start=1): 
        if num == nums[idx-1]+1:
            count += 1
        else:
            answer.add(count) 
            count = 1
    answer.add(count)
    return max(answer, default=None)

print(solution(nums=[100,4,200,1,3,2]))
print(solution(nums=[0,3,7,2,5,8,4,6,0,1]))

# set 쓸 필요 없음. best/cur로 구현하기
def solution2(nums):
    if not nums: return 0
    nums.sort() #[1,2,3,4,100,200], [0,0,1,2,3,4,5,6,7,8]
    best,cur = 1,1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]+1:
            cur += 1
        else:
            best = max(best, cur)
            cur = 1
  
    return max(best,cur) # 배열이 끝났을 때 best 처리 한 번 더 해야함. 

print(solution2(nums=[100,4,200,1,3,2]))
print(solution2(nums=[0,3,7,2,5,8,4,6,0,1]))

# 해시셋으로 풀면 O(n)에 풀 수 있다.
# 아이디어: 모든 수를 set에 넣고, 시작점에서만 길이를 센다. 
def solution3(nums):
    s = set(nums) # {100,4,200,1,3,2}: 순서는 상관없음
    best = 0
    for x in s:
        next = x+1
        while next in s:
            count += 1
            next += 1
      

