# 서울에서김서방찾기 -> https://programmers.co.kr/learn/courses/30/lessons/12919?language=python3

def solution(seoul):
    for i,v in enumerate(seoul):   #i는 number, v는 value를 뽑아낸다.
        if(v == 'Kim'):
            answer='김서방은 '+str(i)+'에 있다'  # str을 안쓰면 문자열로 인식되어 오류나더라 
    return answer


seoul = ['Kim', 'Jane']
