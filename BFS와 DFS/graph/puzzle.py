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

from collections import deque

def solution(game_board, table):
    n = len(game_board)
    dirs=[(0,1),(1,0),(0,-1),(-1,0)] # 오른쪽부터 시계방향 탐색
    
    def collect_puzze_bfs(board, sr, sc, target):
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


    visited=set()
    for r in range(n):
        for c in range(n):
            if table[r][c] == 1 and (r,c) not in visited:
                puzzle = collect_puzze_bfs(table, r, c, 1)
    pass
    