# 프린터(https://programmers.co.kr/learn/courses/30/lessons/42587)
from collections import deque

def solution(priorities, location):
    answer = 0
    priorities_que = deque([(item, pos) for pos, item in enumerate(priorities)])
    while True :
        # 가장 앞의 문서
        item = priorities_que.popleft()
        # 문서가 남아있고 / 만약 지금의 문서가 중요도가 max_item보다 낮다면
        if priorities_que and max(priorities_que)[0] > item[0] :
            # 현재 프린트 순서의 맨 뒤로 보냄
            priorities_que.append(item)
        else :
            # 아닐 경우 순서 + 1
            answer +=1
            # 찾고자 하는 문서 위치가 나오면
            if item[1] == location :
                break
    return answer