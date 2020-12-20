# 내적(https://programmers.co.kr/learn/courses/30/lessons/70128)
def solution(a, b):
    list_len = len(a)
    answer = 0
    for pos in range(list_len):
        answer += a[pos]*b[pos]
    return answer