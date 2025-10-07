'''
표현 가능한 이진트리
'''

# 아이디어
# 1. 노드는 왼쪽부터 오른쪽 (dfs - 중위순회)
# 2. 주어진 number를 먼저 이진수로 변환하기
# 3. 그리고 그 이진수로 포화 트리를 그릴 수 있냐 없느냐를 따질 것

# 포화 트리의 규칙
# 1. 부모 노드는 반드시 1일 것.
# 2. 포화트리의 노드의 갯수는 1,3,7,23 .. 중 하나여야함 f(n) = f(n-1) + 2^n, (n>=1, f(0)=1)


def solution(numbers):
    # 10진수 2진수로 변환
    def decimal_to_binary(num):
        if num == 0 : return "0"

        binary = ""
        while num:
            r = num % 2
            q = num // 2
            binary += str(r)
            num = q
            
        return binary[::-1]
    
    # n_bits를 담을 수 있는 가장 작은 포화 트리의 길이
    def smallest_tree_size(n):
        size = 1
        while size < n:
            size = size*2 + 1
        return size
        
    # 주어진 이진수(bits)로 포화 트리를 구성할 수 있을까? 부모 노드는 반드시 1이어야함
    # 즉, 어떤 노드가 0이면 그 하위 서브 트리에 1이 없어야 함
    def is_valid_tree(bits):
        if len(bits) <= 1: return True
        mid = len(bits)//2
        root = bits[mid]
        left,right = bits[:mid], bits[mid+1:]
        
        # 루트가 0인데 왼쪽/오른쪽 서브트리에 1이 있다면 불가능
        if root == '0' and ('1' in left or '1' in right):
            return False
        
        # binary의 길이가 1이 될때까지 반복! 
        return is_valid_tree(left) and is_valid_tree(right)
        
    
    answer=[]

    # 1) 2진수 변환
    binaries = [decimal_to_binary(x) for x in numbers]
    
    # 2) 2진수 포화 트리 형식에 맞게 변환(왼쪽에 0 추가)
    padded=[b.zfill(smallest_tree_size(len(b))) for b in binaries]
   
    # 3) 유효성 검사
    answer = [1 if is_valid_tree(b) else 0 for b in padded]

    return answer

print(solution(numbers=[7, 42, 5]))