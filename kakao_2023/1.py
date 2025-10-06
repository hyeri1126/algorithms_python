'''
    개인정보 수집 유효기간
'''
def solution(today, terms, privacies):
    answer = []
    term={} # {A:6, B:12, C:3}
    cur_year, cur_month, cur_day = today.split('.')
    cur_year, cur_month, cur_day = int(cur_year), int(cur_month), int(cur_day)
    
    for tm in terms:
        left, right = tm.split()
        term[left]=int(right)
        
    for idx, privacy in enumerate(privacies):
        left, right = privacy.split()
        year, month, day = left.split('.')
        year, month, day =int(year), int(month), int(day)
        month += term[right]
        if month > 12:
            year += (month - 1) // 12
            month = (month - 1)%12 +1 
        if year < cur_year:
            answer.append(idx+1)
        if year == cur_year and month < cur_month:
            answer.append(idx+1)
        if year == cur_year and month == cur_month and day <= cur_day:
            answer.append(idx+1)
    return answer

print(solution(today="2022.05.19", terms=["A 6", "B 12", "C 3"], privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))


'''
    [월 정규화 실수 회고]
    문제 
    - months를 더한 뒤 아래처럼 정규화하면 12의 배수에서 month는 0이 되는 버그가 발생함
      (예: 12월 + 12개월 -> month = 24 % 12 = 0)
    # (오류 코드) 
    a, b = month % 12, month // 12
    month = a  <- 12의 배수일 때 0이 되어버림 (요휴범위 1~12 위반)
    year += b

    원인 
    - 달을 1~12의 1-기반 값임. 단순히 % 12를 사용하면 0-기반처럼 동작해버림
    
    해결
    - 0-기반으로 한 번 내렸다가 다시 1-기반으로 올리는 정규화가 필요

    # (수정 코드)
    year += (month - 1)//12
    month = (month - 1)%12 + 1
'''



# ----- 권장 방식 ------ 
# 모든 달이 28일로 단순화 된 것을 이용해서 날짜를 총일수로 변환해서 푸는 방식이 베스트
def solution2(today, terms, privacies):
    def date_to_days(date):
        y,m,d = map(int, date.split('.'))
        return y*12*28 + m*28 + d 

    today_days=date_to_days(today)
    term = {k: int(v) for k,v in (t.split() for t in terms)}
    answer=[]

    for idx, privacy in enumerate(privacies):
        start, kind = privacy.split()
        end_days=date_to_days(start)+term[kind]*28-1 
        if end_days < today_days:
            answer.append(idx+1)
        
    return answer

print(solution2(today="2022.05.19", terms=["A 6", "B 12", "C 3"], privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))