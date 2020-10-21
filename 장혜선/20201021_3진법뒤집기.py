def solution(n):

# (제한사항) n 자연수 입력(1이상 100,000,000 이하) 체크
    if 1<=n<=100000000 : pass
    else : exit()

# 1. 3진법으로 표현
    # 1-1. 3진법 자릿수 구하기
    # 3의 num 승보다 같거나 클때까지 num자릿수를 키운 다음 out
    # 입력 값(n)은 3의 num 승보다 같거나 작다
    num = 0
    test_val = n
    while True:
        if test_val >= 3**(num):
            num += 1
        else :
            break

    # [0]*(num) 으로 3진법으로 표현할 리스트를 생성
    thd_list = [0]*num

    # 1-2. 3진법 자리(pos)마다 들어갈 숫자 구하기
    # 3^num를 입력값(test_val)에서 뺀 후 0보다 크면 해당 pos 위치의 숫자를 1씩 올린다
    # ------------------ 참고 ------------------
    # (3진법 표현) 구현 편의상 11122 -> [2,2,1,1,1] 으로 표현되게 생성한다.
    # 3^n 에서 인덱스를 n으로 활용하려면 실제 3진법의 반전된 리스트를 생성해야 함
    # 입출력 예처럼 표현하려면 (len(3진법 변수 리스트)-1-n)을 인덱스로 쓰면 된다.
    # -------------------------------------------

    for pos in range(num-1,-1,-1):
        while test_val - 3**(pos) >= 0 :
            test_val = test_val - 3**(pos)
            thd_list[pos] +=1
    # (*)입출력 예처럼 표현하려면: thd_list[(num-1)-pos] +=1

# 2. 3진법 뒤집기
    # 리스트 뒤집기 : a[::-1]
    thd_list = thd_list[::-1]

# 3. 뒤집어진 3진법을 10진법으로 표현하기
    # n번째 자리에 있는 수 * 3의 n승
    answer = 0
    for pos in range(num):
        answer += (thd_list[pos])*(3**pos)
    #(*)입출력 예처럼 표현하려면: (thd_list[(num-1)-pos])*(3**pos)

    return answer
