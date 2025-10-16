'''
    프로그래머스 고득점 - 퍼즐 조각 채우기
    문제: 테이블 위에 높인 퍼즐 조각을 게임 보드의 빈 공간에 적절히 올려놓기. 
    규칙
        1. 조각은 한 번에 하나씩 채워넣기
        2. 조각을 회전시킬 수 있으나 뒤집을 수는 없음
        3. 게임 보드에 새로 채워 넣는 퍼즐 조각과 인접한 칸이 비어있으며 안됨
        
    input: game_board: [[0,0,0],[1,1,0],[1,1,1]], table: [[1,1,1],[1,0,0],[0,0,0]], output: 0 
'''

# 아이디어
# 1. table 순회하면서 퍼즐 조각 puzzles에 담기? 모양이랑 너비도 같이 담겨야하는데.. 모양을 포함해서 어떻게 보관해?
# 2. game_board 순회하면서 빈 곳 보고 빈 칸이 몇 개인지 세워보고.. 빈칸의 수가 퍼즐 조각의 수와 같다면
# 회전해 보면서 넣어보기?


# 아이디어 정답
# 한 조각의 좌표들을 모은 뒤, 튜플 형태 시그니처로 만든다! 즉, 정규화가 포인트!
# 예: {(2,3),(2,4),(3,3)} → 평행이동 → {(0,0),(0,1),(1,0)} → ((0,0),(0,1),(1,0))

from collections import deque,defaultdict

def solution(game_board, table):
    n = len(game_board)
    dirs=[(0,1),(1,0),(0,-1),(-1,0)] # 오른쪽부터 시계방향 탐색
    
    def collect_puzze_by_bfs(board, sr, sc, target):
        q = deque([(sr,sc)])
        visited.add((sr,sc))
        cells=[(sr,sc)]
        while q:
            r,c = q.popleft()
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((nr,nc))
                    cells.append((nr,nc))
        return cells

    # 핵심!!!
    def normalize(cells):
        """좌표들을 (0,0) 기준으로 평행이동하고 정렬하여 튜플 시그니처로"""
        min_r = min(r for r, _ in cells)
        min_c = min(c for _, c in cells)
        norm = sorted((r - min_r, c - min_c) for r, c in cells)
        return tuple(norm)
    
    def rotate90(cells):
        """(r,c)->(c,-r) 회전. 세트/리스트 입력 허용, 결과는 리스트"""
        return [(c, -r) for (r, c) in cells]


    def rotations(signature):
        """정규화된 시그니처(튜플)를 받아 4회전 모든 시그니처(정규화 후)를 생성"""
        # 리스트로 변환
        cells = list(signature)
        # 0°, 90°, 180°, 270°
        rots = []
        cur = cells
        for _ in range(4):
            # 정규화 위해 리스트 -> normalize
            rots.append(normalize(cur))
            # 다음 회전
            cur = rotate90(cur)
        # 중복 제거(모양이 대칭이면 중복 가능)
        return list(dict.fromkeys(rots))

    visited=set()
    holes=[]
    for r in range(n):
        for c in range(n):
            if table[r][c] == 1 and (r,c) not in visited:
                puzzle = collect_puzze_by_bfs(table, r, c, 1)
                
    visited = set()
    pieces_by_size = defaultdict(list)
    for r in range(n):
        for c in range(n):
            if table[r][c] == 1 and (r, c) not in visited:
                cells = collect_puzze_by_bfs(table, r, c, 1)
                sig = normalize(cells)
                pieces_by_size[len(sig)].append(sig)
                
    answer = 0
    for hole in holes:
        size = len(hole)
        if not pieces_by_size[size]:
            continue

        # 구멍의 4회전(사실 구멍은 회전할 필요 없지만, 조각/구멍 어느 쪽을 돌려도 무방)
        # 보통은 "조각"만 4회전하며 비교하는 편이 직관적이지만,
        # 구현을 단순하게 하기 위해 아래처럼 '조각'의 4회전 집합을 만들어 비교.
        found_index = -1
        target_rots = set(rotations(hole))  # 구멍 모양의 가능한 시그니처들 (4회전)
        # 조각 후보들 순회
        for i, piece in enumerate(pieces_by_size[size]):
            piece_rots = set(rotations(piece))
            if target_rots & piece_rots:
                found_index = i
                break
        if found_index != -1:
            # 사용한 조각 제거
            pieces_by_size[size].pop(found_index)
            answer += size

    return answer
    