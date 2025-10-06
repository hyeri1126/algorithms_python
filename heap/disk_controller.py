'''
    프로그래머스 고득점 - 디스크 컨트롤러
    우선순위 디스크 컨트롤러는 다음과 같이 동작한다
        1. 작업의 번호, 작업의 요청 시각, 작업의 소요시간을 저장해 두는 대기 큐가 존재
        2. 하드 디스크가 작업을 하고 있지 않고 대기 큐가 비어있다면 우선순위가 가장 높은 작업을 대기 큐에서 꺼낸 후, 하드디스크에 그 작업을 시킨다
           (우선순위: 작업의 소요시간이 짧은 것 > 작업의 요청 시간이 빠른 것 > 작업의 번호가 작은 것)
        3. 하드 디스크는 한 번에 하나의 작업만 수행한다
        4. 하드 디스크의 작업이 끝나면 디스크 컨트롤러는 요청을 대기 큐에 저장한 후, 대기 큐에서 작업을 꺼내온다.
    ** 제약 조건 **
        1 <= len(jobs) <= 500 -> 시간복잡도는 n^3 까지 가능하겠는데?
        jobs[i]=[s,l] (s는 요청되는 시점, ㅣ은 작업의 소요시간)
            0 <= s <= 10^3
            1 <= l <= 10^3
    input: jobs=[[0, 3], [1, 9], [3, 5]], ouput: 3
'''


# ----- 첫 번째 풀이 ------
import heapq

def solution(jobs):
    n = len(jobs)
    
    total = 0
    # jobs=[(s, l, i) for i, (s, l) in enumerate(jobs)] # jobs에 job 번호 추가한 버전
    jobs=sorted([(s, l, i) for i, (s, l) in enumerate(jobs)], key=lambda x: x[0])

    pq=[] # (작업시간, 요청 시각, 작업 번호) 저장
    heapq.heapify(pq)
    cur_time=0
    done = 0
    i=0
    
    while done < n:
        while i<n and jobs[i][0] <= cur_time:
            heapq.heappush(pq, (jobs[i][1], jobs[i][0], jobs[i][2])) # 우선순위 반영해서 priority queue에 저장
            i += 1 
        
        while pq: # pq가 없어질 때까지 한번에 pop 하는게 아니라.. 한번 pop 하고 매번 들어오는거 있나 동시에 확인해야함.. 
            cur_job_time, cur_job_start, cur_job_num = heapq.heappop(pq) # 꺼냈으면 바로 하드 디스크에 넘기기
            done += 1
            cur_time += cur_job_time
            total+=(cur_time - cur_job_start)
            
        if i<n and not pq and cur_time < jobs[i][0]:
            cur_time = jobs[i][0]
        
    return int(total//n)

print(solution(jobs=[[0, 3], [1, 9], [3, 5]]))
print(solution(jobs=[[2,3]]))

# 시간 초과 -> 원인: 무한루프.. pq가 비어있고 cur_time이 늘지 않아서 영원히 멈춤... if i< n and not pq: 추가해서 해결
# 도착 순으로 jobs를 정렬해야함 -> 당연히 도착 순으로 줄거라고 생각했는데.. 이걸 또 정렬하라고 하다니;



# ------ 두번째 풀이 -------
# 위 코드처럼 pq에 있는걸 한번에 pop 하면 안됨.. 한 번에 하나의 일만 pop... 그리고 또 들어올거 있나 확인 그리고 또 팝 그리고 또 들어올 거 있나 확인.. 이런식..
def solution2(jobs):
    n = len(jobs)
    
    total = 0
    # jobs=[(s, l, i) for i, (s, l) in enumerate(jobs)] # jobs에 job 번호 추가한 버전
    jobs=sorted([(s, l, i) for i, (s, l) in enumerate(jobs)], key=lambda x: x[0])

    pq=[] # (작업시간, 요청 시각, 작업 번호) 저장
    heapq.heapify(pq)
    cur_time=0
    done = 0
    i=0
    
    while done < n:
        while i<n and jobs[i][0] <= cur_time:
            heapq.heappush(pq, (jobs[i][1], jobs[i][0], jobs[i][2])) # 우선순위 반영해서 priority queue에 저장
            i += 1 
        
        if not pq:
            cur_time = jobs[i][0] # 대기큐 비어있으면 다음 job 도착 시간으로 점프! (더하고 그런거 x...)
            continue
                    
        cur_job_length, cur_job_start, cur_job_num = heapq.heappop(pq) # 꺼냈으면 바로 하드 디스크에 넘기기
        done += 1
        cur_time += cur_job_length
        total+=(cur_time - cur_job_start)
        
    return int(total//n)

print(solution2(jobs=[[0, 3], [1, 9], [3, 5]]))
print(solution2(jobs=[[2,3]]))




# 너무 어렵다,,,, ㅏ