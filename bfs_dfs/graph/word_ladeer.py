# Word Ladder
# 단어의 한 글자만 바꾸며 시작 단어에서 목표 단어로 가장 짧게 가는 변환 길이는?

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    q=deque()
    q.append((begin,0))
    visited=set([begin])
    def diff_by_str(a,b):
        diff=0
        for ch1,ch2 in zip(a,b):
            if ch1 != ch2:
                diff+=1
            if diff > 1:
                return False
        return diff == 1    
    while q:
        curr_word,d=q.popleft()
        if curr_word == target:
            return d
        for word in words:
            if word not in visited and diff_by_str(curr_word,word):
                visited.add(word)
                q.append((word,d+1))
    return 0

print(solution(begin="hit",target="cog",words=["hot", "dot", "dog", "lot", "log", "cog"]))