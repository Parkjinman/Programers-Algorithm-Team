# 문자열 내 p와 y의 개수(https://programmers.co.kr/learn/courses/30/lessons/12916)
def solution(s):
    # 앞에서부터 순회하면서
    p = 0
    y = 0
    for word in s :
        # p/P나 y/Y를 만나면 1씩 더하고
        if word in ['p', 'P']:
            p += 1
        elif word in ['y', 'Y']:
            y += 1
        else :
            pass
    
    # 갯수가 같으면 True 
    if p == y :
        return True
    # 다르면 False
    else :
        return False