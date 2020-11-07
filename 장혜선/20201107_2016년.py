# 2016년(https://programmers.co.kr/learn/courses/30/lessons/12901)
def solution(a, b):

    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month =[0,31,29,31,30,31,30,31,31,30,31,30,31]

    # 각 월별 일 수를 누적하여 합산하고
    # 일자에 해당하는 수-1 을 더한 다음 (예: 2월 1일은 1월 1일로부터 31일 뒤이고, 2월 3일은 1월 1일로부터 31+2일 뒤)
    # 7로 나눈 나머지로 요일 찾음(기준일 1월 1일 (금), 7일 뒤(7로 나눈 나머지 0)는 금요일)
    answer = day[(sum(month[:a])+b-1)%7]

    return answer
