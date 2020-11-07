# 주식가격(https://programmers.co.kr/learn/courses/30/lessons/42584)
from collections import deque
# 효율성 문제로 파이썬 리스트 대신 deque를 사용(큐) 
# (popleft의 시간복잡도 O(1)가 리스트의 pop(0) 보다 낮음 O(n))
def solution(prices):
    # 정답을 담을리스트, 전체 길이, 주가리스트(큐)
    answer = []
    len_now = len(prices)
    prices = deque(prices)

    while True :
        if prices : # 비교할 주가가 남아있으면
            #맨 앞 주가 popleft()
            now_price = prices.popleft()
            #현재길이(len_now) : 전체 길이 -1
            len_now -=1
    
            #1이면 무조건 len_now append(남은 기간 전체동안 안 떨어짐)  
            if now_price == 1:
                answer.append(len_now)
            
            else :
                pos_aft = 0
                while True:
                    try : 
                        if now_price > prices[pos_aft] : # now_price보다 작다면
                            #현재 위치+1(가격이 안떨어진 기간) 리턴
                            answer.append(pos_aft+1)
                            break
                        else : # 크거나 같다면 다음 위치로 이동
                            pos_aft +=1
                    except : # 끝까지 가면 len_now append(남은 기간 전체동안 안 떨어짐)  
                        answer.append(len_now)
                        break
        else : # 주가 비교가 끝나면 (prices에 남은 원소 X)
            return answer