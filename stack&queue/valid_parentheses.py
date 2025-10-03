'''
    괄호 유효성 문제
    '(){}[]'를 포함하고 있는 문자열 s가 주어졌을 때, 괄호가 유효한지 아닌지 판별하시오.
    *제약조건* 
        1 <= s.length <= 10^4 -> 시간복잡도는 n^2 보다 효율적으로 해야함
        문자열 s는 '()[]{}'의 괄호 들로만 구성되어 있다.
    input: s=")(" output: false
    input: s="([]}" output: false
    input: s="{()[]}" output: true
''' 

# point: stack에 넣으려는데 top의 값이 나와 짝꿍이라면 붙어있다면 빼고 그게 아니면 계속 추가하기
# 시간 복잡도: O(n), n은 문자열 s의 길이
# + 보통 list가 input으로 주어진다면 확인하는 절차만 수행해도 O(n)이 걸림. 따라서 O(n)으로 풀리면 최적이라 봐도 무방
def solution(s):
    stack=[]
    for chr in s:
        if not stack : 
            stack.append(chr)
            continue
        if chr == ')' : 
            if stack[-1] == '(' :
                stack.pop()
                continue
        if chr == ']':
            if stack[-1] == '[':
                stack.pop()
                continue
        if chr == '}':
            if stack[-1] == '{':
                stack.pop()
                continue
        stack.append(chr)
    print(stack)
    return not stack # stack이 비어있으면 True, 아니면 False

print(solution(s="{()[]}"))
print(solution(s="([]}"))
print(solution(s=")("))

# --- 1차 수정 -- 
def solution2(s):
    stack=[]
    for chr in s:
        if chr in '({[': # 여는 괄호면 바로 push
            stack.append
            continue
        # 닫는 괄호 처리 
        if chr == ')' : 
            if not stack or stack[-1] != '(' :
                return False
            stack.pop()
            continue
        if chr == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
            continue
        if chr == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()
            continue
        
    return not stack 


# 강의 해설
def isValid(s):
    stack=[]
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
        return not stack