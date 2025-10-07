'''
    2023 카카오 코테 - 표 병합
    input: commands: ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
    output: ["d", "EMPTY"]
'''

def solution(commands):
    answer = []
    content=[[""]*51 for _ in range(51)] # 50행 50열 contentrix 생성 -> content를 담고 있음!
    # merge했던 정보도 따로 가지고 있어야 할 것 같은데?  -> 대표 좌표를 저장하는 이차원 리스트가 필요, 처음엔 자기 자신
    merged=[[(r,c) for c in range(51)] for r in range(51) ]

    
    def update_cell(r,c,value):
        y,x = merged[r][c]
        content[y][x] = value 

    def update_value(value1, value2):
        # 그냥 반복문 돌아서 value1 있으면 싹 다 value2로 바꿀까? 루트 노드는 신경 안 써도 되나?
        # 아.. 어차피 루트 노드만 값을 가진다! 이게 포인트.. 
        for i in range(51):
            for j in range(51):
                if content[i][j] == value1:
                    content[i][j] = value2
            
    def merge(r1,c1,r2,c2):
        if (r1,c1) == (r2,c2) : return
        # 부모가 가지고 있는 실제 값 가져오기!
        y1,x1 = merged[r1][c1]
        y2,x2 = merged[r2][c2]
        
        # 이미 같은 그룹이면 아무 것도 하지 말고 종료
        if (y1,x1) == (y2, x2):
            return
        
        v1, v2 = content[y1][x1], content[y2][x2]
        
        # b 그룹 전체를 a 그룹으로 치환
        for i in range(51):
            for j in range(51):
                if merged[i][j] == (y2,x2):
                    merged[i][j] = merged[r1][c1] # merged[r2][c2]를 부모로 가지던 모든 애들 찾아서 부모 merged[r1][c1]으로 바꿔주기! 
      
        # 값 결정
        content[y1][x1] = v1 or v2
            
        # 그리고 r2,c2가 가지고 있던 Content는 없애야겠는데?
        # ** 주의 ** content[r2][c2]를 비우는게 아니라 부모의 content를 초기화해야함.. 
        content[y2][x2] = "" # 빈 문자열로 초기화
            
    
    def unmerge(r,c):
        y,x = merged[r][c]
        keep = content[y][x]
        for i in range(51):
            for j in range(51):
                if merged[i][j] == (y,x):
                    merged[i][j] = (i,j) # 자긴 자신을 루트로 갖도록 바꾸고
                    content[i][j] = "" # content도 초기화!
        # (r,c)는 원래 가지고 있던 content를 유지해야함!
        content[r][c] = keep

    def print(r,c):
        y,x = merged[r][c]
        if content[y][x] : answer.append(content[y][x])
        else: answer.append("EMPTY")
       
        
    for command in commands:
        type = command.split()[0]
        if type == "UPDATE":
            num = len(command.split())
            if num == 4:
                param1, r, c, value = command.split()
                update_cell(int(r), int(c), value)
            else:
                param1, value1, value2 = command.split()
                update_value(value1, value2)
        elif type == "MERGE":
            param1, r1, c1, r2, c2 = command.split()
            merge(int(r1), int(c1), int(r2), int(c2))
        elif type == "UNMERGE":
            param1, r, c = command.split()
            unmerge(int(r),int(c))
        elif type == "PRINT":
            param1, r, c = command.split()
            print(int(r),int(c))
    
    return answer


print(solution(commands=["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"])) # output: ["d", "EMPTY"]
print(solution(commands=["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))