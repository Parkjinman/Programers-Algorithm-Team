# 올바른 괄호(https://programmers.co.kr/learn/courses/30/lessons/12909)
def solution(s):
    # ) 로 시작하면 무조건 False
    # bucket 생성(dummy로 '0'을 생성)
    bucket = ['0']
    if s[0] == ')' : 
        return False
    
    # ( 로 시작했을 때 
    else :
        for item in s :
            # 첫 괄호를 담을 때 예외처리를 하지 않기 위해 dummy로 '0' 넣어둠
            # 직전 괄호와 지금의 괄호를 합쳐서 ()가 되면 직전 괄호를 빼낸다 
            # 지금 괄호는 넣지 않음 (한쌍의 괄호 완성)
            if bucket[-1]+item == '()':
                bucket.pop()
            else :
                # 합쳐서 ()가 되지 않으면 bucket에 담는다.
                bucket.append(item)
        # 마지막까지 돌았을 때 bucket에 1개만 남으면(처음에 dummy로 넣은 '0') True
        if len(bucket) == 1 : 
            return True
        # 남아있다면 False
        else :
            return False