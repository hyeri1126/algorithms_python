'''
    Daily Temperatures
    매일의 온도를 나타내는 int형 배열 temperatures가 주어진다. answer 배열의 원소 answer[i]는 i번 째 날의 온도보다
    더 따뜻해지기까지 며칠을 기다려야하는지 나타낸다. 만약 더 따뜻해지는 날이 없다면 answer[i] == 0 이다.
    answer 배열을 반환하는 함수를 구하시오.
    ** 제약조건 **
        1 <= temperatures.length <= 10^5 -> 시간복잡도는 n^2보다 작아야한다
        30 <= temperaturs[i] <= 100 -> 별 의미 없어보인다
    input: temperatures=[73,74,75,71,69,72,76,73], output: [1,1,4,2,1,0,0]
    input: temperatures=[30,40,50,60], output: [1,1,1,0]
'''

# 가장 먼저 생각나는 방법은 이중반복문.. 시간복잡도는 O(n^2) 여서 시간초과임
def solution(temperatures):
    answer=[0]*len(temperatures)
    for i in range(len(temperatures)-1):
        for j in range(i+1,len(temperatures)):
            if temperatures[i] < temperatures[j]:
                answer[i]=j-i
                break
    return answer

print(solution(temperatures=[73,74,75,71,69,72,76,73]))


# 최적화 필요함 
# 정렬할까? temperatures의 순서를 지켜야하기 때문에 정렬 x
# 이전값보다 큰 값이 나타나는 순간 그 전값들에 영향을 줌
# 그니까 이전값보다 큰 값이 나타나기 전까지 stack에 온도를 쌓다가 큰 값 나타나면 작은 값 전부 pop?
def solution2(temperatures):
    stack=[]
    answer=[0]*len(temperatures)
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day,_ = stack.pop()
            answer[prev_day]= cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return answer

print(solution2(temperatures=[73,74,75,71,69,72,76,73]))