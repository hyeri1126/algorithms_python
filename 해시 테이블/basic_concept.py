'''
    Hash Table
    정의: 효율적인 탐색(빠른 탐색)을 위한 자료구조로써 key-value 쌍의 데이터를 입력받는다. hash fuction h에
    key값을 입력으로 넣어 얻은 해시값 h(k)를 위치로 지정하여 key-value 데이터 쌍을 저장한다. 저장,삭제,검색의 시간복잡도는 O(1)이다.
    1. Array List based Hash Table (충돌해결방법: Open addressing)
    2. Array List + Linked List based Hash Table (충돌해결방법: Seperate Chaining)
    ** 파이썬에서는 dictionary 자료구조가 Hash Table로 구현된 것이다. 파이썬의 dictionary는 1번이다. **
'''



'''
    Dictionary: 파이썬의 Dictionary는 Hash Table로 구현되었다.
    코딩테스트에서 Dictionary는 시간 복잡도를 줄이기 위해 메모리를 사용하는 것이다.
    사용 방법) student[2022937]="류혜리"
    -> 코드 실행 시 내부적으로는 key값을 hash function에 넣어서 index 값을 구하고 해당 index에 key-value를 추가하는 것이지만
    실제 사용할 때는 key값을 index처럼 생각해서 사용하면 됨!
'''

# Dictionary 활용 예시
score=[97, 49, 89] # 단점: 97점은 무슨 과목인지 모름 -> dictionary 활용!
# dictionary 선언
score={}
# dictionary 선언 및 초기화
score={
    'math': 97,
    'eng': 49,
    'kor': 89
} # value값이 무엇을 의미하는지 훨씬 알아보기 쉬움
# dictionary 접근
print(score['math']) 
# dictionary 수정
score['math'] = 45 # 값을 덮어씌움
# dictionary 추가
score['sci'] = 100
# score['music'] # KeyError: value가 존재하지 않는 Key에 접근 시 에러 발생

# dictionary에 key가 존재하는지 확인하고 싶을 때
print('music' in score)
if 'music' in score: # random access 
    print(score['music'])
else:
    score['music'] = 0
    
    

# dictionary 기본 활용 문제
# Two sum
# 완전 탐색으로 풀 시 시간복잡도는 n^2 -> 리스트를 정렬한 후, two pointer를 사용해서 문제 해결했었음 시간복잡도는 O(nlogn)
# 메모리를 사용한다면? 
def twosum(nums,target):
    memo={} # dict 대신 set을 써도 됨
    for num in nums:
        need = target - num 
        if need in memo:
            return True
        memo[num]=True 
    return False
print(twosum(nums=[4,1,9,7,5,3,16], target=14))
print(twosum(nums=[2,1,5,7], target=4))

# set vs dict
# 존재 여부만 확인하는 경우 set 사용 -> Two sum은 존재 여부만 알면 되기 때문에 set을 쓰는게 맞음
# 인덱스/위치가 필요하다면 dict 사용
# set과 dict의 내부는 둘 다 해시 테이블이라 삽입은 O(1)의 시간이 걸리고 멤버십 테스트는 O(1)