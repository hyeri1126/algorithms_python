'''
    프로그래머스 알고리즘 고득점 - Heap
    각 음식의 scoville 지수를 알려주는 scoville=[1, 2, 3, 9, 10, 12]이 주어졌을 때, 모든 음식의 스코빌 지수를 K로 만들고 싶다면 몇번
    음식을 섞어야 하는지 return 하시오.
    섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    ** 제한 사항 **
        2 <= len(scoville) <= 10^6 -> 시간복잡도 n^2 보다 작아야함 
        0 <= K <= 10^9 
        0 <= scoiville[i] <= 10^6
        모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 하시오
'''

# 처음 접근법 - 반복문 + 재정렬하기(sort())
def solution(scoville, K):
    cnt = 0
    for _ in range(len(scoville)-1):
        if all(x > K for x in scoville): return cnt
        scoville.sort()
        scoville.append(scoville[0]+(scoville[1]*2))
        scoville.pop(0)
        scoville.pop(0)
        cnt += 1
    return cnt if scoville[0] >= K else -1

print(solution(scoville=[1, 2, 3, 9, 10, 12], K=7))
print(solution(scoville=[5, 1, 4, 2], K=7)) 
print(solution(scoville=[1, 1], K=100))

# 결과: 정확성 모두 통과, 효율성 모두 실패 
# 시간 복잡도: 반복문 n-1회, 반복문 한 번 내에서 scoville의 길이를 m이라고 한다면 T(i) = O(m) + O(mlogm) + O(1) + O(m)= O(mlogm) => O(n^2logn)





# 두 번째 접근법 - prioriy queue 사용하기
import heapq
def solution2(scoville, K):
    n = len(scoville)
    heapq.heapify(scoville) 
    cnt = 0
    for _ in range(n-1):
        # if all(x>=K for x in scoville): return cnt -> scoville의 첫 번째 값만 확인하면 됨
        if scoville[0] >= K : return cnt
        a = heapq.heappop(scoville) 
        b = heapq.heappop(scoville)
        new = a + b*2
        heapq.heappush(scoville, new)
        cnt += 1
    return cnt if scoville[0] >= K else -1


print(solution2(scoville=[1, 2, 3, 9, 10, 12], K=7)) # 2
print(solution2(scoville=[5, 1, 4, 2], K=7)) # 3
print(solution2(scoville=[1, 1], K=100)) # -1


# 결과: 정확성 전부 통과, 유효성 전부 통과, 시간복잡도: O(n^2)
# heapify -> O(n), 반복문 루프: 최대 n-1회, 반복문 내: O(1)+ 3*O(logm) = O(logm) => 총 O(nlogn)  