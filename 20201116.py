# Programers-Algorithm-Team
프로그래머스 알고리즘 기록
import datetime  #datetime 라이브러리 사용

def solution(month, day) :
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'] 
    dval = datetime.date(2016, month, day)  #2016년 고정
    wval = dval.weekday()  #정수형으로 요일값 반환
    answer = week[wval]    #0 = MON 이므로
    return answer
    
print(solution( 5, 24))
