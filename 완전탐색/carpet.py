def solution(brown, yellow):
    total = brown + yellow  # 전체 칸 수

    # 전체 넓이 total의 약수 h를 전부 시험해봄
    for h in range(1, int(total**0.5) + 1):
        if total % h != 0:
            continue  # h가 약수가 아니면 패스

        w = total // h  # 가로는 전체/세로

        # 테두리 제외한 내부(yellow)가 맞는지 확인
        # 최소한 테두리를 만들려면 가로,세로 >=3 이어야 함
        if w >= 3 and h >= 3 and (w - 2) * (h - 2) == yellow:
            return [w, h]  # 가로 먼저